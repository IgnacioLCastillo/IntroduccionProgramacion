miUsuario='ICastillo'
miClave='Jornada2022'
bloqueoIntentos=3
miIntento=''
misErrores=0

while misErrores<bloqueoIntentos and miClave!=miIntento:
    print('-'*30,'LOGIN PAGE','-'*30,)
    print(f"UserName:{miUsuario}")
    miIntento=input("Password:")
    if miClave!=miIntento:
        misErrores+=1
        print(f"Clave Incorrecta quedan:{bloqueoIntentos-misErrores}")
    else:
        print (f"{miUsuario} - Acceso Exitoso")

if misErrores==3:
    print (f"{miUsuario} - Bloqueo de Usuario")
