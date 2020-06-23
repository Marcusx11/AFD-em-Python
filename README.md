# AFD-em-Python

  O presente projeto é uma implementação minha de um AFD (Autômato Finito Determinístico) realizada em Python.

# O que é um AFD?

  Dando uma breve explicação sobre o que é um AFD. Um AFD é uma máquina de estados finita que aceita ou rejeita uma cadeia de caracteres que é lhe dada por um "input". A partir do estado inicial, percorre-se cada símbolo desta cadeia, fazendo com que chegue-se a um outro estado após o "consumo" deste caractere. Se depois de consumir toda a cadeia, o estado atual estiver na lista de estados finais do autômato, é considerado que ele "aceita" esta cadeia, e caso contrário, signiica que ele "não a aceita". Um AFD é uma quíntupla, composto por:
  * Um conjunto finito de símbolos de "input" chamado de "alfabeto" do autômato.
  * Um conjunto finito de estados.
  * Uma função de transição, a qual diz: A partir de um estado "Q", se eu consumir um símbolo do alfabeto, eu chego em um estado "W".
  * Um estado inicial, do qual começará a percorrer o autômato a partir deste estado.
  * Um conjunto de estados finais de aceitação.

Vale lembrar que a cadeia dada como "input" deve conter apenas símbolos que estão presentes no conjunto do alfabeto do autômato e as transições deve possuir apenas estados que estão presente no conjunto finito de estados (O código trata estes casos).

# Considerações finais

  Esta é uma implementação simples de um AFD, fique a vontade em utilizá-la para fins acadêmicos e caso ache algum erro que passou despercebido ou algo do tipo, envie-me uma mensagem falando sobre para que eu possa corrigi-lo.
 
