from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector
import os

app = Flask(__name__)
app.secret_key = "dev-secret"  # troque para produção

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASS", "root"),
    "database": os.getenv("DB_NAME", "exemplo_flask"),
    "port": int(os.getenv("DB_PORT", "3306")),
}

def get_conn():
    return mysql.connector.connect(**DB_CONFIG)

@app.route("/")
def index():
    # lista produtos
    conn = get_conn()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM produtos ORDER BY id DESC")
    produtos = cur.fetchall()
    cur.close()
    conn.close()
    return render_template("index.html", produtos=produtos)

@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        nome = request.form.get("nome")
        preco = request.form.get("preco")
        if not nome or not preco:
            flash("Preencha todos os campos.", "danger")
            return redirect(url_for("create"))
        try:
            conn = get_conn()
            cur = conn.cursor()
            cur.execute("INSERT INTO produtos (nome, preco) VALUES (%s, %s)", (nome, preco))
            conn.commit()
            cur.close()
            conn.close()
            flash("Produto criado com sucesso!", "success")
            return redirect(url_for("index"))
        except Exception as e:
            flash(f"Erro ao criar produto: {e}", "danger")
            return redirect(url_for("create"))
    return render_template("create.html")

@app.route("/edit/<int:pid>", methods=["GET", "POST"])
def edit(pid):
    conn = get_conn()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM produtos WHERE id = %s", (pid,))
    produto = cur.fetchone()
    cur.close()
    conn.close()
    if not produto:
        flash("Produto não encontrado.", "warning")
        return redirect(url_for("index"))
    if request.method == "POST":
        nome = request.form.get("nome")
        preco = request.form.get("preco")
        if not nome or not preco:
            flash("Preencha todos os campos.", "danger")
            return redirect(url_for("edit", pid=pid))
        try:
            conn = get_conn()
            cur = conn.cursor()
            cur.execute("UPDATE produtos SET nome=%s, preco=%s WHERE id=%s", (nome, preco, pid))
            conn.commit()
            cur.close()
            conn.close()
            flash("Produto atualizado com sucesso!", "success")
            return redirect(url_for("index"))
        except Exception as e:
            flash(f"Erro ao atualizar: {e}", "danger")
            return redirect(url_for("edit", pid=pid))
    return render_template("edit.html", produto=produto)

@app.route("/delete/<int:pid>", methods=["POST"])
def delete(pid):
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("DELETE FROM produtos WHERE id = %s", (pid,))
        conn.commit()
        cur.close()
        conn.close()
        flash("Produto deletado!", "success")
    except Exception as e:
        flash(f"Erro ao deletar: {e}", "danger")
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
