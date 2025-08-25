executando = True
import conversor

while executando:
  print("Escolha a conversão: \n1-Pé para metro \n2-Metros para Pé\n3-Jarda para Metros\n4-Jarda para Pé\n5-Encerrar programa")
  escolha = int(input("Digite sua escolha: "))
  
  match escolha:
    case 1:
      pe = float(input("Quantos pes: "))
      metro = conversor.pe_para_metro(pe)
      print(metro)
      
    case 2:
      metro = float(input("Quantos metros: "))
      pe = conversor.metro_para_pe(metro)
      print(pe)
      
    case 3:
      jarda = float(input("Quantas jardas: "))
      metro = conversor.jarda_para_metro(jarda)
      print(metro)

    case 4:
      jarda = float(input("Digite quantas jardas: "))
      pe = conversor.jarda_para_pe(jarda)
      print(pe)

    case 5:
      executando = False

    case _:
      print("opção invalida tente novaente")