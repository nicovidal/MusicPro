from transbank.webpay.webpay_plus.transaction import Transaction
from transbank.webpay.webpay_plus.transaction import TransactionCreateResponse

# Configuración de las credenciales de Webpay
commerce_code = 597055555532
api_key = '579B532A7440BB0C9079DED94D31EA1615BACEB56610332264630D42D0A36B1C'
integration_type = "TEST"  # Puedes utilizar "LIVE" para producción

# Crear una nueva transacción
transaction = Transaction.create(
    buy_order="orden_de_compra",
    session_id="identificador_de_sesion",
    amount=1000,  # Monto de la transacción en pesos chilenos
    return_url="https://tu_url_de_retorno.com",
    final_url="https://tu_url_final.com",
    commerce_code=commerce_code,
    api_key=api_key,
    integration_type=integration_type,
)

# Obtener la URL de redirección a Webpay para completar el pago
redirect_url = transaction.get_redirect_url()

# Redireccionar al cliente a la URL de Webpay
# Esto debe realizarse en tu aplicación web o en el flujo de pago correspondiente
print("Redirecciona al cliente a la siguiente URL:")
print(redirect_url)
