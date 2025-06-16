class Producto:
    def __init__(self, pro_empresa, pro_codigo, pro_id, pro_nombre):
        self.PRO_EMPRESA = pro_empresa
        self.PRO_CODIGO = pro_codigo
        self.PRO_ID = pro_id
        self.PRO_NOMBRE = pro_nombre

    @staticmethod
    def from_tuple(data):
        return Producto(*data)
