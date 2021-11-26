# Extração e tratamento de dados com Python do MySQL Workbench para o SQL Server

Essa integração foi criada com intuito de melhorar a eficiência e velocidade de uma extração de dados através de um SELECT no MySQL Workbench de uma empresa e inserção desse SELECT tratado dentro do SQL Server de outra empresa.

Utilizei o bulk insert dentro da procedure no SQL Server para poder melhorar o tempo de inserção dos dados dentro do banco.

Observação: o bulk insert requer que o CSV esteja dentro do servidor do banco de dados final.
