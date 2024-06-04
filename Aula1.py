import pandas as pd

lista_nomes = 'Howard Ian Peter Jonah Kellie'.split()
lista_cpfs = '111.111.111-11 222.222.222-22 333.333.333-33 444.444.444-44 555.555.555-55'.split()
lista_emails = 'risus.varius@dictumPhasellusin.ca Nunc@vulputate.ca fames.ac.turpis@cursusa.org non@felisullamcorper.org eget.dictum.placerat@necluctus.co.uk'.split()
lista_idades = [32, 22, 25, 29, 38]
pd.DataFrame(lista_nomes, columns=['nome'])

# Criando o DataFrame
df = pd.DataFrame({
    'Nome': lista_nomes,
    'CPF': lista_cpfs,
    'Email': lista_emails,
    'Idade': lista_idades
})

# Exibindo o DataFrame
print(df)

#SELEÇÃO DE COLUNAS EM UM DATAFRAME(parei aqui)

