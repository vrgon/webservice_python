# webservice_python
Webservice in python

# Webservice de consulta(GET) e inserção(POST) via json em Python

# install
pip install - r requirements.txt


# As conexões estão substituidas por arquivos csv, substitu-as pela sua conexão e tabelas no banco. (Esta incluso também coneção com mysql)

# Padrão de consulta json
Inserir no Headers as Key login, password com value cnpj e senha

no Body enviar o json no formato:
<pre>

{    
 "produto":[
              {   
                "Codproduto": "7899",
                "Descricao": "teste1",
                "Codbarra": "",
                "Ncm": "",
                "Exncm": "",
                "Cstent": "",
                "Cstsai": "",
                "Unidmedida": "",
                "Cest": "",
                "Icmscstent": "",
                "Icmscstsai": ""
              },  
              {   
                "Codproduto": "7894900559002",
                "Descricao": "test1",
                "Codbarra": "",
                "Ncm": "",
                "Exncm": "",
                "Cstent": "",
                "Cstsai": "",
                "Unidmedida": "",
                "Cest": "",
                "Icmscstent": "",
                "Icmscstsai": ""
              },
              {   
                "Codproduto": "78915628",
                "Descricao": "aaaaaaa",
                "Codbarra": "",
                "Ncm": "",
                "Exncm": "",
                "Cstent": "",
                "Cstsai": "",
                "Unidmedida": "",
                "Cest": "",
                "Icmscstent": "",
                "Icmscstsai": ""
              },
              {   
                "Codproduto": "78915628",
                "Descricao": "aaaaaaa",
                "Codbarra": "",
                "Ncm": "",
                "Exncm": "",
                "Cstent": "",
                "Cstsai": "",
                "Unidmedida": "",
                "Cest": "",
                "Icmscstent": "",
                "Icmscstsai": ""
              },
              {   
                "Codproduto": "71181245",
                "Descricao": "aaaaaaa",
                "Codbarra": "",
                "Ncm": "",
                "Exncm": "",
                "Cstent": "",
                "Cstsai": "",
                "Unidmedida": "",
                "Cest": "",
                "Icmscstent": "",
                "Icmscstsai": ""
              },
              {   
                "Codproduto": "78915628",
                "Descricao": "aaaaaaa",
                "Codbarra": "",
                "Ncm": "",
                "Exncm": "",
                "Cstent": "",
                "Cstsai": "",
                "Unidmedida": "",
                "Cest": "",
                "Icmscstent": "",
                "Icmscstsai": ""
              },
              {   
                "Codproduto": "78999999",
                "Descricao": "aaaaaaa",
                "Codbarra": "",
                "Ncm": "",
                "Exncm": "",
                "Cstent": "",
                "Cstsai": "",
                "Unidmedida": "",
                "Cest": "",
                "Icmscstent": "",
                "Icmscstsai": ""
              },
              {   
                "Codproduto": "78915628",
                "Descricao": "aaaaaaa",
                "Codbarra": "",
                "Ncm": "",
                "Exncm": "",
                "Cstent": "",
                "Cstsai": "",
                "Unidmedida": "",
                "Cest": "",
                "Icmscstent": "",
                "Icmscstsai": ""
              }
              
              ] 
          
}
</pre>
