import mysql.connector

#FUNÇÃO PARA CONECTAR O BANCO

def connect():
    return mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "unip",
        database = "unip"
    )

def criar_usuario(nome, email):
    db = connect()
    cursor = db.cursor()
    sql = "INSERT INTO usuarios (nome, email) VALUES (%s,%s)"
    values = (nome, email)
    cursor.execute(sql, values)
    db.commit()
    print(cursor.rowcount,"Usuário criado com sucesso!")
    db.close()
    # INSERT INTO usuarios (nome, email) VALUES (nome, email) => sintaxe SQL
    #INSERT INTO table (campo1, campo2...) VALUES (valor1, valor2)

def listar_usuarios() :
    db = connect()
    cursor = db.cursor()
    sql = "SELECT * FROM usuarios" 
    cursor.execute(sql,)
    result = cursor.fetchall()
    for linha in result :
        print(linha)
    db.close
    
    #sql = "SELECT * FROM usuarios"
    # SELECT * FROM usuarios
    # SELECT * FROM table

def atualizar_usuario(id, nome, email):
    db = connect()
    cursor = db.cursor()
    sql = "UPDATE usuarios SET nome = %s, email = %s WHERE id = %s"
    values = (nome, email, id)
    cursor.execute(sql,values)
    db.commit()
    print(cursor.rowcount,"Usuário atualizado com sucesso")
    db.close
    
    #UPDATE table SET campo1 = valor1, campo2 = valor2, ..., campoN = valorN WHERE ID = ID
    #UPDATE usuarios SET nome = "nome", email = "email" WHERE id = id
    #UPDATE usuario SET nome = %s, email = %s WHERE id = %s

def excluir_usuario(id):
    db = connect()
    cursor = db.cursor()
    sql = "DELETE FROM usuarios WHERE id = %s"
    values = (id,)
    cursor.execute(sql,values)
    db.commit()
    print(cursor.rowcount,"usuario deletado!")
    db.close
    
    # DELETE FROM usuarios - deleta TODOS os registros
    #DELETE FROM usuarios WHERE campo = valor - deleta APENAS um valor

if __name__ == "__main__":
    while True:
        print("\n ==== MENU CRUD ====")
        print("\n1 - Criar usuário")  
        print("2 - Listar usuário")
        print("3 - Atualizar usuário")
        print("4 - Excluir usuario")
        print("5 - sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            nome = input("Nome:")
            email = input("Email: ")
            criar_usuario(nome, email)
    
        elif opcao == "2":
            listar_usuarios()
            
        elif opcao == "3":
            listar_usuarios()
            id = input("Selecione o ID do usuário para atualizar: ")
            nome = input("Novo nome: ")
            email = input("Novo email: ")
            atualizar_usuario(id, nome, email)
            
        elif opcao ==  "4":
            listar_usuarios()
            id = input("ID do usuário a excluir: ")
            excluir_usuario(id)
                           
        elif opcao == "5":
            print("Saindo")
            break
           
#CRUD - Create, Read, Update e Delete