from hashlib import sha256

usuario_padrao = "685f82f0a38130835b1a050bca1ddffff6a7282f35fdb88408bb0cea4ffcd774"
senha_padrao = "03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4"

usuario_digitado = str(input("Digite seu usuário: ")).encode("ascii")
senha_digitado = str(input("Digite sua senha: ")).encode("ascii")

usuario_digitado = sha256(usuario_digitado).hexdigest()#pega o conteudo do objeto
senha_digitado = sha256(senha_digitado).hexdigest()

if usuario_digitado == usuario_padrao and senha_digitado == senha_padrao:
    print("Bem vindo a Fatec")
else:
    print("Senha ou usuário incorreto")


