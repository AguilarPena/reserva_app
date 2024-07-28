def get_cadastro():
    with open("reserva_app/usuarios.csv", mode="r") as usuarios2:
        usuarios = [] 
        for linha in usuarios2: 
            reserva_app_usuario = linha.strip().split(",") 
            linha = {
                "nome": reserva_app_usuario[0],
                "email": reserva_app_usuario[1], 
                "senha": reserva_app_usuario[2],
                "codigo": reserva_app_usuario[3],
                "admin": reserva_app_usuario[4]
            }
            usuarios.append(linha)
            return usuarios

def save_cadastro(nome, email, senha,codigo, admin):
    with open("reserva_app/usuarios.csv", "a", encoding="utf8") as usuarios2: 
        usuarios =  f"{nome},{email},{senha},{codigo},{admin}"
        usuarios2.write(f"{usuarios}\n")

def get_salas():
    with open("reserva_app/salas.csv", mode="r", encoding="utf8") as salas2:
        salas = [] 
        for linha in salas2: 
            reserva_app_salas = linha.strip().split(",")
            linha = {
                "codigo": reserva_app_salas[0],
                "tipo": reserva_app_salas[1],
                "descricao": reserva_app_salas[2],
                "capacidade": reserva_app_salas[3],
                "ativo": reserva_app_salas[4]
            }
            salas.append(linha)
    return salas


        
def save_salas(codigo, tipo, descricao, capacidade, ativo):
    with open("reserva_app/salas.csv", "a", encoding="utf8") as salas2: 
        salas =  f"{codigo},{tipo},{descricao},{capacidade},{ativo}"
        salas2.write(f"{salas}\n")

def get_reservas():
    with open("reserva_app/reservas.csv", mode="r", encoding="utf8") as reservas2:
        reservas = [] 
        for linha in reservas2: 
            reserva_app_reservas = linha.strip().split(",") 
            linha = {
                "codigo": reserva_app_reservas[0],
                "sala": reserva_app_reservas[1], 
                "d_início": reserva_app_reservas[2],
                "d_fim": reserva_app_reservas[3],
                "admin": reserva_app_reservas[4],
                "ativo": reserva_app_reservas[5]
            }
            reservas.append(linha)
    return reservas

def save_reserva(codigo, sala, d_inicio, d_fim, admin, ativo):
     with open("reserva_app/reservas.csv", "a", encoding="utf8") as reservas2: 
        reservas =  f"{codigo},{sala},{d_inicio},{d_fim},{admin},{ativo}"
        reservas2.write(f"{reservas}\n")
