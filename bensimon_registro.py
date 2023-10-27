class registro:
    btn_popup_id = "closeBtn" 
    txt_email_id = "email"
    txt_password_id = "pass"
    btn_ingresar_xpath = "//*[@id='send2']"

class busqueda:
    dpd_search_xpath = "//*[@id='search']"
    btn_search_xpath = "//*[@id='search_mini_form']/div[2]/button"
    txt_busqueda_link_text = "LLAVERO PVC B NEGRO"
    txt_busqueda = "Resultados de búsqueda para: 'llaveros'"
    txt_busqueda2 = "Resultados de búsqueda para: 'camisas'"

class producto1_carrito:
    btn_talle_id = "option-label-talle-533-item-38"
    btn_comprar_id = "product-addtocart-button"
    txt_compra = "Agregaste LLAVERO PVC B NEGRO a tu carrito de compras."
    txt_compra_xpath = "//*[@id='maincontent']/div/div/div[1]/div[2]/div[2]/div/div/div"
    btn_carrito_xpath = "//*[@id='html-body']/div[3]/header/div[3]/div[2]/a/span[2]/span[1]"
    txt_producto_carrito_xpath = "//header/div[3]/div[2]/div[1]/div[1]/div[1]/div[2]/div[4]/ol[1]/li[1]/div[1]/div[1]/strong[1]/a[1]"
    dpd_detalles_xpath = "//span[contains(text(),'Ver detalles')]"
    dpd_ver_editar_xpath = "//*[@id='minicart-content-wrapper']/div[2]/div[5]/div/a/span"
    txt_color_xpath = "//*[@id='shopping-cart-table']/tbody[1]/tr[1]/td[1]/div/dl/dd[1]"

class carrito_compras:
    txt_pagina = "Carrito de compras"
    dpd_cantidad_xpath = "/html/body/div[3]/main/div[3]/div/div[3]/form/div[1]/table/tbody/tr[1]/td[3]/div/div/label/input"
    btn_actualizar_xpath = "//*[@id='form-validate']/div[2]/button"
    txt_cantidad_xpath = "//*[@id='cart-92494-qty']"
    txt_talle_xpath = "//*[@id='shopping-cart-table']/tbody/tr[1]/td[1]/div/dl/dd[2]"
    dpd_homepage_xpath = "/html/body/div[3]/header/div[1]/a/img"

class producto2_carrito :
    txt_producto2_link_text = "CAMISA TOKYO CUADROS ML"
    btn_color_id = "option-label-color-277-item-177"
    btn_talle_id = "option-label-talle-533-item-37"
    txt_compra2 = "Agregaste CAMISA TOKYO CUADROS ML a tu carrito de compras."
    txt_talle_xpath = "//*[@id='shopping-cart-table']/tbody[2]/tr[1]/td[1]/div/dl/dd[2]"
    txt_color_xpath = "//*[@id='shopping-cart-table']/tbody[2]/tr[1]/td[1]/div/dl/dd[1]"
    btn_finalizar_compra_xpath = "//*[@id='maincontent']/div[3]/div/div[3]/div[1]/ul/li/button"
    txt_checkout = "Checkout"