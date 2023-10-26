from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import configparser
from bensimon_registro import *
import pytest

class sprint3_user2(unittest.TestCase):

    def setUp(self):
        configuracion = configparser.ConfigParser()
        configuracion.read('Configuracion.ini')
        configuracion.sections()
        self.page = configuracion['Paginas']['Page']
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
    
    
    def test_case_1073(self):
        driver = self.driver
        driver.get(self.page)
        time.sleep(3)
        #Cerrar el pop-up
        pop_up = driver.find_element(By.ID, registro.btn_popup_id)
        pop_up.click()
        time.sleep(2)
        #Login de usuario
        driver.find_element(By.ID, registro.txt_email_id).send_keys('eugetmarbelo@gmail.com')
        driver.find_element(By.ID, registro.txt_password_id).send_keys('Arbelo123.')
        ingresar = driver.find_element(By.XPATH, registro.btn_ingresar_xpath)
        ingresar.click()
        time.sleep(2)
        #Carrito de compras
        carrito = driver.find_element(By.XPATH, producto1_carrito.btn_carrito_xpath)
        carrito.click()
        time.sleep(3)
        wait = WebDriverWait(driver, 10)
        titulo_producto = wait.until(EC.presence_of_element_located((By.XPATH, producto1_carrito.txt_producto_carrito_xpath ))).text
        self.assertEqual(busqueda.txt_busqueda_link_text, titulo_producto, "El producto en carrito no coincide")

        ver_editar_carrito = driver.find_element(By.XPATH, producto1_carrito.dpd_ver_editar_xpath)
        ver_editar_carrito.click()

        titulo_pagina = driver.title
        self.assertEqual(carrito_compras.txt_pagina, titulo_pagina, "La página no corresponde al carrito de compras")
        time.sleep(3)

       # Borrar la cantidad actual (1) y escribir (3)
        cantidad = driver.find_element(By.XPATH, carrito_compras.dpd_cantidad_xpath)
        time.sleep(2)
        cantidad.clear()
        time.sleep(2)
        cantidad.send_keys('3')
        time.sleep(3)

        # Hacer clic en el botón "Actualizar carrito"
        actualizar = driver.find_element(By.XPATH, carrito_compras.btn_actualizar_xpath )
        actualizar.click()
        time.sleep(10)

        cantidad_esperada_carrito = '3'
        leyenda_cantidad_carrito = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/main/div[3]/div/div[3]/form/div[1]/table/tbody[1]/tr[1]/td[3]/div/div/label/input"))).get_attribute('value')

        if cantidad_esperada_carrito == leyenda_cantidad_carrito:
            self.assertTrue(True, "La cantidad de productos en el carrito coincide")
        else:
            self.assertTrue(False, f"La cantidad de productos en el carrito no coincide. Se esperaba {cantidad_esperada_carrito}, pero se encontró {leyenda_cantidad_carrito}")

        producto_en_carrito = busqueda.txt_busqueda_link_text
        nombre_producto_carrito = wait.until(EC.presence_of_element_located((By.LINK_TEXT, busqueda.txt_busqueda_link_text))).text
        self.assertEqual(producto_en_carrito, nombre_producto_carrito, "El producto que se encuentra en el carrito no coincide con el producto agregado")

        if producto_en_carrito == nombre_producto_carrito:
            self.assertTrue(True, "El nombre del producto en el carrito coincide con el producto seleccionado")
        else:
            self.assertTrue(False, f"El nombre del producto en el carrito no coincide. Se esperaba {producto_en_carrito}, pero se encontró {nombre_producto_carrito}")

        talle_esperado_carrito = "UN"
        talle_en_carrito = wait.until(EC.presence_of_element_located((By.XPATH, carrito_compras.txt_talle_xpath ))).text
        self.assertEqual(talle_esperado_carrito, talle_en_carrito, "El talle no coincide con lo seleccionado")

        if talle_en_carrito == talle_esperado_carrito:
            self.assertTrue(True, "El talle de producto en el carrito coincide con el talle seleccionado")
        else:
            self.assertTrue(False, f"El talle del producto en el carrito no coincide. Se esperaba {talle_esperado_carrito}, pero se encontró {talle_en_carrito}")
        time.sleep(2)
        #Nuevamente a la home page
        driver.find_element(By.XPATH, carrito_compras.dpd_homepage_xpath ).click()
        time.sleep(2)
    
    def test_case_1082(self):
        driver = self.driver
        driver.get(self.page)
        time.sleep(3)
        #Cerrar el pop-up
        pop_up = driver.find_element(By.ID, registro.btn_popup_id)
        pop_up.click()
        time.sleep(2)
        driver.find_element(By.ID, registro.txt_email_id).send_keys('eugetmarbelo@gmail.com')
        driver.find_element(By.ID, registro.txt_password_id).send_keys('Arbelo123.')
        ingresar = driver.find_element(By.XPATH, registro.btn_ingresar_xpath)
        ingresar.click()
        time.sleep(2)

        #Bensimon home page
        home_page = driver.find_element(By.XPATH, carrito_compras.dpd_homepage_xpath).click()
        time.sleep(5)
       
        buscador = driver.find_element(By.XPATH, busqueda.dpd_search_xpath).send_keys('camisas')
        Lupa_buscador = driver.find_element(By.XPATH, busqueda.btn_search_xpath)
        Lupa_buscador.click()
        titulo_pag = driver.title
        self.assertEqual("Resultados de búsqueda para: 'camisas'", titulo_pag, "No coincide con la búsqueda efectuada")
        time.sleep(3)

        camisa = driver.find_element(By.LINK_TEXT, producto2_carrito.txt_producto2_link_text ).click()
        time.sleep(2)
        color_camisa = driver.find_element(By.ID, producto2_carrito.btn_color_id).click()
        time.sleep(2)
        talle_camisa = driver.find_element(By.ID, producto2_carrito.btn_talle_id ).click()
        time.sleep(3)
        

        boton_comprar = driver.find_element(By.ID, producto1_carrito.btn_comprar_id)
        boton_comprar.click()

        wait = WebDriverWait(driver, 10)
        mensaje_esperado = producto2_carrito.txt_compra2
        #Esperar a que el mensaje aparezca y obtener su texto
        leyenda_compra = wait.until(EC.presence_of_element_located((By.XPATH, producto1_carrito.txt_compra_xpath))).text
        # Realizar la aserción
        self.assertEqual(mensaje_esperado, leyenda_compra, "El mensaje de compra no coincide")
        time.sleep(3)

        carrito = driver.find_element(By.XPATH, producto1_carrito.btn_carrito_xpath)
        carrito.click()
        time.sleep(3)

        ver_editar_carrito = driver.find_element(By.XPATH, producto1_carrito.dpd_ver_editar_xpath)
        ver_editar_carrito.click()

        titulo_pagina = driver.title
        self.assertEqual(carrito_compras.txt_pagina, titulo_pagina, "La página no corresponde al carrito de compras")
        time.sleep(3) 
    
    def test_case_1083(self):
        driver = self.driver
        driver.get(self.page)
        time.sleep(3)
        #Cerrar el pop-up
        pop_up = driver.find_element(By.ID, registro.btn_popup_id)
        pop_up.click()
        time.sleep(2)
        driver.find_element(By.ID, registro.txt_email_id).send_keys('eugetmarbelo@gmail.com')
        driver.find_element(By.ID, registro.txt_password_id).send_keys('Arbelo123.')
        ingresar = driver.find_element(By.XPATH, registro.btn_ingresar_xpath)
        ingresar.click()
        time.sleep(2)

        carrito = driver.find_element(By.XPATH, producto1_carrito.btn_carrito_xpath)
        carrito.click()
        time.sleep(3)

        ver_editar_carrito = driver.find_element(By.XPATH, producto1_carrito.dpd_ver_editar_xpath)
        ver_editar_carrito.click()

        titulo_pagina = driver.title
        self.assertEqual(carrito_compras.txt_pagina, titulo_pagina, "La página no corresponde al carrito de compras")
        time.sleep(3)

        wait = WebDriverWait(driver, 10)
        #Validaciones de los productos en el carrito
        #Producto 1 = Llaveros
        cantidad_esperada_carrito = '3'
        leyenda_cantidad_carrito = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/main/div[3]/div/div[3]/form/div[1]/table/tbody[1]/tr[1]/td[3]/div/div/label/input"))).get_attribute('value')

        if cantidad_esperada_carrito == leyenda_cantidad_carrito:
            self.assertTrue(True, "La cantidad de llaveros en el carrito coincide")
        else:
            self.assertTrue(False, f"La cantidad de llaveros en el carrito no coincide. Se esperaba {cantidad_esperada_carrito}, pero se encontró {leyenda_cantidad_carrito}")

        producto_en_carrito = busqueda.txt_busqueda_link_text
        nombre_producto_carrito = wait.until(EC.presence_of_element_located((By.LINK_TEXT, busqueda.txt_busqueda_link_text))).text
        self.assertEqual(producto_en_carrito, nombre_producto_carrito, "El primer producto que se encuentra en el carrito no coincide con el producto esperado")

        if producto_en_carrito == nombre_producto_carrito:
            self.assertTrue(True, "El nombre del primer producto en el carrito coincide con el producto seleccionado")
        else:
            self.assertTrue(False, f"El nombre del primer producto en el carrito no coincide. Se esperaba {producto_en_carrito}, pero se encontró {nombre_producto_carrito}")

        color_esperado_carrito = "NEGRO"
        color_en_carrito = wait.until(EC.presence_of_element_located((By.XPATH, producto1_carrito.txt_color_xpath))).text
        self.assertEqual(color_esperado_carrito, color_en_carrito, "El color del producto no coincide con lo seleccionado")

        if color_en_carrito == color_esperado_carrito:
            self.assertTrue(True, "El color del primer producto en el carrito coincide con el color seleccionado")
        else:
            self.assertTrue(False, f"El color del primer producto en el carrito no coincide. Se esoperaba {color_esperado_carrito}, pero se encontró {color_en_carrito}")
        time.sleep(2)

        talle_esperado_carrito = "UN"
        talle_en_carrito = wait.until(EC.presence_of_element_located((By.XPATH, carrito_compras.txt_talle_xpath ))).text
        self.assertEqual(talle_esperado_carrito, talle_en_carrito, "El talle no coincide con lo seleccionado")

        if talle_en_carrito == talle_esperado_carrito:
            self.assertTrue(True, "El talle del primer producto en el carrito coincide con el talle seleccionado")
        else:
            self.assertTrue(False, f"El talle del primer producto en el carrito no coincide. Se esperaba {talle_esperado_carrito}, pero se encontró {talle_en_carrito}")
        time.sleep(2)

         #Producto 2 = Camisa Tokyio
        cantidad_esperada_carrito2 = '1'
        leyenda_cantidad_carrito2 = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/main/div[3]/div/div[3]/form/div[1]/table/tbody[2]/tr[1]/td[3]/div/div/label/input"))).get_attribute('value')

        if cantidad_esperada_carrito2 == leyenda_cantidad_carrito2:
            self.assertTrue(True, "La cantidad de camisas en el carrito coincide")
        else:
            self.assertTrue(False, f"La cantidad de camisas en el carrito no coincide. Se esperaba {cantidad_esperada_carrito2}, pero se encontró {leyenda_cantidad_carrito2}")

        producto_en_carrito2 = producto2_carrito.txt_producto2_link_text
        nombre_producto_carrito2 = wait.until(EC.presence_of_element_located((By.LINK_TEXT, producto2_carrito.txt_producto2_link_text))).text
        self.assertEqual(producto_en_carrito2, nombre_producto_carrito2, "El segundo producto que se encuentra en el carrito no coincide con el producto esperado")

        if producto_en_carrito2 == nombre_producto_carrito2:
            self.assertTrue(True, "El nombre del segundo producto en el carrito coincide con el producto seleccionado")
        else:
            self.assertTrue(False, f"El nombre del segundo producto en el carrito no coincide. Se esperaba {producto_en_carrito2}, pero se encontró {nombre_producto_carrito2}")

        color_esperado_carrito2 = "VERDE"
        color_en_carrito2 = wait.until(EC.presence_of_element_located((By.XPATH, producto2_carrito.txt_color_xpath))).text
        self.assertEqual(color_esperado_carrito2, color_en_carrito2, "El color del producto no coincide con lo seleccionado")

        if color_en_carrito2 == color_esperado_carrito2:
            self.assertTrue(True, "El color del segundo producto en el carrito coincide con el color seleccionado")
        else:
            self.assertTrue(False, f"El color del segundo producto en el carrito no coincide. Se esoperaba {color_esperado_carrito2}, pero se encontró {color_en_carrito2}")
        time.sleep(2)
        
        talle_esperado_carrito2 = "EXTRA LARGE"
        talle_en_carrito2 = wait.until(EC.presence_of_element_located((By.XPATH,    producto2_carrito.txt_talle_xpath ))).text
        self.assertEqual(talle_esperado_carrito2, talle_en_carrito2, "El talle no coincide con lo seleccionado")

        if talle_en_carrito2 == talle_esperado_carrito2:
            self.assertTrue(True, "El talle del segundo producto en el carrito coincide con el talle seleccionado")
        else:
            self.assertTrue(False, f"El talle del segundo producto en el carrito no coincide. Se esperaba {talle_esperado_carrito2}, pero se encontró {talle_en_carrito2}")
        time.sleep(2)   
    
        color_esperado_carrito2 = "VERDE"
        color_en_carrito2 = wait.until(EC.presence_of_element_located((By.XPATH,    producto2_carrito.txt_color_xpath))).text
        self.assertEqual(talle_esperado_carrito2, talle_en_carrito2, "El talle no coincide con lo seleccionado")

        if talle_en_carrito2 == talle_esperado_carrito2:
            self.assertTrue(True, "El talle del segundo producto en el carrito coincide con el talle seleccionado")
        else:
            self.assertTrue(False, f"El talle del segundo producto en el carrito no coincide. Se esperaba {talle_esperado_carrito2}, pero se encontró {talle_en_carrito2}")
        time.sleep(2)  

        driver.get_screenshot_as_file("C:\\Users\\Fiorella\\Documents\\Testing QA PIL 2023\\Sprint 3\\Carrito_compras.png") 

        #Finalizar compra
        btn_finalizar = driver.find_element(By.XPATH, producto2_carrito.btn_finalizar_compra_xpath)
        btn_finalizar.click()
        time.sleep(2)

        titulo_checkout = driver.title
        self.assertEqual(producto2_carrito.txt_checkout, titulo_checkout, "La página no corresponde al checkout para finalizar compra")
        time.sleep(3)
                
    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()




 

