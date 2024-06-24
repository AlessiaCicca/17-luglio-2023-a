from database.DB_connect import DBConnect
from model.connessione import Connessione
from model.prodotto import Prodotto


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getColori():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct gp.Product_color as colore
from go_products gp """

        cursor.execute(query)

        for row in cursor:
            result.append(row["colore"])

        cursor.close()
        conn.close()
        return result
    @staticmethod
    def getNodi(colore):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct gp.*
from go_products gp
where gp.Product_color=%s"""

        cursor.execute(query,(colore,))

        for row in cursor:
            result.append(Prodotto(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getConnessioni(colore,anno):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select t2.p2 as v1,t1.p1 as v2, count(distinct t1.d1) as peso
from (select gds.Retailer_code as r1, gds.Product_number as p1, gds.`Date` as d1
from go_daily_sales gds,go_products gp 
where year(gds.`Date`)=%s and gp.Product_Number=gds.Product_number and gp.Product_color=%s)as t1,
(select gds.Retailer_code as r2, gds.Product_number as p2, gds.`Date` as d2
from go_daily_sales gds, go_products gp 
where year(gds.`Date`)=%s and gp.Product_Number=gds.Product_number and gp.Product_color=%s)as t2
where t1.r1=t2.r2 and t2.p2!=t1.p1 and t1.d1=t2.d2
group by t2.p2,t1.p1 """

        cursor.execute(query,(anno,colore,anno,colore,))

        for row in cursor:
            result.append(Connessione(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getProdotti():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select *
    from go_products gp
  """

        cursor.execute(query)

        for row in cursor:
            result.append(Prodotto(**row))

        cursor.close()
        conn.close()
        return result
