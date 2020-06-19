# webservice_python
Webservice in python

Webservice de consulta e inserção via json em Python
As conexões estão substituidas por arquivos csv, substitu-as pela sua coneção e tabelas no banco. (Esta incluso também coneção com mysql)

Padrão de consulta json
Inserir no Headers as Key login, password com value cnpj e senha

no Body enviar o json no formato:


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

