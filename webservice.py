from flask import Flask, url_for,request, jsonify
from flask_restful import Resource, Api, reqparse
import mysql.connector
import pandas as pd
from typing import List
import json



def check_user(cnpj,senha):
    conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="12345",
            database="erp1"
            )

    sql = '''SELECT id_cliente, cnpj, wsenha
        FROM cliente
        WHERE cliente.cnpj = '''+ cnpj +'''
        
        '''
    #df = pd.read_sql_query(sql = sql, con = conn)
    df = pd.read_csv("cliente.csv")
    conn.close()
    return df




#################################################       JSON        ###################################
class Produto(object):
    def __init__(self, coditen_cli: str, descricao: str,codbarras: str,ncm: str):
        self.coditen_cli = coditen_cli
        self.descricao = descricao
        self.codbarras = codbarras
        self.ncm = ncm

class Products(object):
    def __init__(self, produto: List[Produto]):
        self.produto = produto

class ProdutoError(object):
    def __init__(self, response: str):
        self.response = response

class ProductsError(object):
    def __init__(self, response: List[ProdutoError]):
        self.response = response


#########################################################################################################




#################################################       SQL CONSULTA        ##############################

def consult_prod(cods_prod, id_cliente):
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        passwd="12345",
        database="erp1",
        charset='latin1',
        use_unicode=True
    )

    df = pd.DataFrame()
    dfc = pd.DataFrame()
    sql = '''
                Select
                    produtos.coditen_cli,
                    produtos.descricao,
                    produtos.codbarras,
                    produtos.ncm,
                    produtos.ex_ncm,
                    relacao_piscofins.natu_tabela,
                    relacao_piscofins.natu_codnature,
                    relacao_piscofins.cst_in,
                    relacao_piscofins.cst_out,
                    relacao_piscofins.aliq_in_pis,
                    relacao_piscofins.aliq_out_pis,
                    relacao_piscofins.aliq_in_cofins,
                    relacao_piscofins.aliq_out_cofins,
                    produtos.conferido,
                    relacao_cestncm2.cest,
                    relacao_icms2.cst_in As cst_in_icms,
                    relacao_icms2.cst_out As cst_out_icms,
                    relacao_icms2.aliq_in As aliq_in_icms,
                    relacao_icms2.aliq_out As aliq_out_icms,
                    relacao_icms2.bc_dentro,
                    relacao_icms2.bc_fora,
                    relacao_cson.cson
                From
                    produtos
                    Inner Join
                    cliente On cliente.id_cliente = produtos.id_cliente
                    Left Join
                    relacao_piscofins On (produtos.ncm = relacao_piscofins.ncm) And
                        (produtos.ex_ncm = relacao_piscofins.ex_ncm) And (cliente.cumulativo =
                        relacao_piscofins.cumulativo)
                    Left Join
                    relacao_cestncm2 On produtos.ncm = relacao_cestncm2.ncm
                    Left Join
                    relacao_icms2 On produtos.ncm = relacao_icms2.ncm
                    Left Join
                    relacao_cson On relacao_icms2.cst_out = relacao_cson.cst
                Where
                    (produtos.id_cliente = '''+ str(id_cliente) +''') And
                    (produtos.coditen_cli in ( '''+ str(cods_prod).strip('[]') +'''))
        '''

    #dfc = pd.read_sql_query(sql = sql, con = conn)
    dfc = df = pd.read_csv("consult_prod.csv")
    df = df.append(dfc, ignore_index = True)
    conn.close()    
    return df



#########################################################################################################




#################################################       SQL CADASTRO        ##############################

def cad_prods(prods_to_insert):

    prods_to_insert = str(prods_to_insert).replace('[','(').replace(']',')')
    prods_to_insert = prods_to_insert[1:-1]
    sql = '''
        INSERT INTO produtos_js_ws (id_cliente,
                                    coditen_cli,
                                    coditen,
                                    descricao,
                                    codbarras_cli,
                                    ncm_cli,
                                    ex_cli,
                                    cst_in_piscofins_cli,
                                    cst_out_piscofins_cli,
                                    unid_inv,
                                    cest,
                                    icms_cst_in,
                                    icms_cst_out                                    
                                    )
        VALUES '''+str(prods_to_insert).replace('[','(').replace(']',')')+''';
    '''
    try:
        conn = mysql.connector.connect(
                                        host="127.0.0.1",
                                        user="root",
                                        passwd="12345",
                                        database="erp1",
                                        charset='latin1',
                                        use_unicode=True
                                    )
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        
    except mysql.connector.Error as error:
        return "PRODUTO NAO CADASTRADO ERRO: {}".format(error)

    return "PROD|1|PRODUTOS CADASTRADOS COM SUCESSO"



#########################################################################################################


def check_prod(id_cli,cod_to_check):

    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        passwd="12345",
        database="erp1",
        charset='latin1',
        use_unicode=True
    )

    df = pd.DataFrame()
    sql = '''
                Select
                    produtos_js_ws.coditen_cli
                From
                    produtos_js_ws
                Where
                    (produtos_js_ws.id_cliente = '''+ str(id_cli) +''') And
                    (produtos_js_ws.coditen_cli = '''+ str(cod_to_check)+''')
        '''
    #df = pd.read_sql_query(sql = sql, con = conn)
    df = pd.read_csv("check_prod.csv")
    conn.close()
    if df.empty:
        return False
    else:
        return True
   
















app = Flask(__name__)




@app.route('/consultaprodutos', methods = ['GET'])
def consulta_produto():
    
    if request.headers['Content-Type'] == 'application/json':
        login = request.headers['login']
        password = request.headers['password']
        client = check_user(login,password)
        if client.empty == False:
            if client.loc[0]['wsenha'] == password:
                pass
            else:
                return 'Senha incorreta'
        else:
            return 'Cliente NAO encontrado'


    if request.method == 'GET':
        rjson = request.get_json()
        products = rjson['produto']
        cod_to_check =[]
        for prod in products:
            if prod['Codproduto'] != '':
                cod_to_check.append(prod['Codproduto'])

        client_id = client.loc[0]['id_cliente']
        df_prod = consult_prod(cod_to_check, client_id)

        prods_to_json = []

        for i,v in df_prod.iterrows():
            prods_to_json.append(Produto(coditen_cli=str(v['coditen_cli']),
                            descricao=v['descricao'],
                            codbarras=v['codbarras'],
                            ncm = str(v['ncm'])
            ))
        
        if df_prod.empty:
            r =['Produto Nao Encontrado']
            jsprod = ProductsError(response=r)
            jsprod = json.dumps(jsprod, default=lambda o: o.__dict__)
            return jsprod
        else:
                
            prods_to_json = Products(produto=prods_to_json)
            json_data_prod = json.dumps(prods_to_json, default=lambda o: o.__dict__, indent=4)

            
            return json_data_prod










        
@app.route('/cadprodutos', methods = ['POST'])
def cadastro_produto():
    if request.headers['Content-Type'] == 'application/json':
        login = request.headers['login']
        password = request.headers['password']
        client = check_user(login,password)
        if client.empty == False:
            if client.loc[0]['wsenha'] == password:
                pass
            else:
                return 'Senha incorreta'
        else:
            return 'Cliente NAO encontrado'

    client_id = client.loc[0]['id_cliente']

    if request.method == 'POST':
        rjson = request.get_json()
        products = rjson['produto']
        prods_to_insert = []
        prods_error = []

        mensagem = []

        for prod in products:
            

            if prod['Codproduto'] == '':
                mensagem = 'ERRO|107|PRODUTO NAO LOCALIZADO E NAO FOI POSSIVEL CADASTRAR '+str(prod)+ ' POR FALTA DO CODIGO DO ITEM'
                prods_error.append(mensagem)
                continue

            elif len(prod['Codproduto']) > 14:
                mensagem = 'ERRO|109|NAO FOI POSSIVEL CADASTRAR '+str(prod)+ ' CODIGO DO PRODUTO MAIOR QUE 14 DIGITOS'
                prods_error.append(mensagem)
                continue
            elif check_prod(client_id,prod['Codproduto']) == False:
                prod_to_list = [client_id]
                prod_to_list.append(prod['Codproduto'])
                prod_to_list.append(prod['Codproduto'].zfill(14))
            elif check_prod(client_id,prod['Codproduto']) == True:
                mensagem = 'PROD|2|PRODUTO '+str(prod)+ ' AGUARDANDO LIBERAÇÃO'
                prods_error.append(mensagem)
                continue


                
            
            
            if len(prod['Descricao']) > 200:
                mensagem = 'ERRO|110|NAO FOI POSSIVEL CADASTRAR '+str(prod)+ ' DESCRIÇÃO DO PRODUTO MAIOR QUE 200 CARACTER'
                prods_error.append(mensagem)
                continue
            else:
                prod_to_list.append(prod['Descricao'])

            if len(prod['Codbarra']) > 14:
                mensagem = 'ERRO|111|NAO FOI POSSIVEL CADASTRAR CODIGO DE BARRA MAIOR QUE 14 DIGITOS '
                prods_error.append(mensagem)
                continue
            else:
                prod_to_list.append(prod['Codbarra'])   

            if len(prod['Ncm']) > 8:
                mensagem = 'ERRO|112|NAO FOI POSSIVEL CADASTRAR '+str(prod)+ ' NCM MAIOR QUE 8 DIGITOS'
                prods_error.append(mensagem)
                continue
            else: 
                prod_to_list.append(prod['Codbarra']) 

            if len(prod['Exncm']) > 3:
                mensagem = 'ERRO|113|NAO FOI POSSIVEL CADASTRAR '+str(prod)+ ' EX NCM MAIOR QUE 3 DIGITOS'
                prods_error.append(mensagem)
                continue
            else: 
                prod_to_list.append(prod['Codbarra'])
            
            if len(prod['Cstent']) > 3:
                mensagem = 'ERRO|114|NAO FOI POSSIVEL CADASTRAR '+str(prod)+ ' CST DE ENTRADA MAIOR QUE 3 DIGITOS'
                prods_error.append(mensagem)
                continue
            else: 
                prod_to_list.append(prod['Codbarra'])

            if len(prod['Cstsai']) > 3:
                mensagem = 'ERRO|115|NAO FOI POSSIVEL CADASTRAR '+str(prod)+ ' CST DE SAIDA MAIOR QUE 3 DIGITOS'
                prods_error.append(mensagem)
                continue
            else: 
                prod_to_list.append(prod['Codbarra'])

            if len(prod['Unidmedida']) > 6:
                mensagem = 'ERRO|116|NAO FOI POSSIVEL CADASTRAR '+str(prod)+ ' UNIDADE DE MEDIDA MAIOR QUE 6 CARACTERE'
                prods_error.append(mensagem)
                continue
            else: 
                prod_to_list.append(prod['Codbarra'])

            if len(prod['Cest']) > 7:
                mensagem = 'ERRO|117|NAO FOI POSSIVEL CADASTRAR '+str(prod)+ ' CEST MAIOR QUE 7 CARACTERES'
                prods_error.append(mensagem)
                continue
            else: 
                prod_to_list.append(prod['Codbarra'])

            if len(prod['Icmscstent']) > 3:
                mensagem = 'ERRO|118|NAO FOI POSSIVEL CADASTRAR '+str(prod)+ ' CST ENTRADA ICMS MAIOR QUE 3 CARACTERE'
                prods_error.append(mensagem)
                continue
            else: 
                prod_to_list.append(prod['Codbarra'])

            if len(prod['Icmscstsai']) > 3:
                mensagem = 'ERRO|119|NAO FOI POSSIVEL CADASTRAR '+str(prod)+ ' CST SAIDA ICMS MAIOR QUE 3 CARACTERES '
                prods_error.append(mensagem)
                continue
            else: 
                prod_to_list.append(prod['Codbarra'])



            prods_to_insert.append(prod_to_list)

        if prods_error != []:
            if prods_to_insert != []:
                r = cad_prods(prods_to_insert) +str(prods_error)
                jsprod = ProductsError(response=r)
                jsprod = json.dumps(jsprod, default=lambda o: o.__dict__)
                return jsprod
            else:
                jsprod = ProductsError(response=str(prods_error))
                jsprod = json.dumps(jsprod, default=lambda o: o.__dict__)
                return jsprod

            
        else:
            #return cad_prods(prods_to_insert)
            return 'ok'
    



@app.route("/webservice")
def index():
    return 'Olá!'



if __name__ == '__main__':
    app.debug = True
    app.run()
    
