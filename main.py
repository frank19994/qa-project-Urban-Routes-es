import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code


class UrbanRoutesPage:
    campo_desde = (By.ID, 'from')
    campo_hasta = (By.ID, 'to')
    boton_pedirtaxi = (By.CSS_SELECTOR, '.button.round')
    imagen_comfort = (By.XPATH, "//div[contains(@class, 'tcard') and .//div[text()='Comfort']]")
    boton_numero_telefono = (By.CLASS_NAME, 'np-button')
    ingresar_numero_telefono = (By.ID, 'phone')
    tipo_tarifas =  (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]')
    boton_siguiente = (By.CSS_SELECTOR, '.button.full')
    codigo_sms = (By.ID, 'code')
    boton_confirmar = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[2]/form/div[2]/button[1]')
    metodo_pago = (By.CLASS_NAME, 'pp-text')
    agregar_metodo_pago = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/div[2]/div[3]')
    ingresa_numero_tarjeta = (By.ID, 'number')
    ingresa_codigo_tarjeta = (By.XPATH, '//div[@class="card-code-input"]/input[@id="code"]')
    agregar_tarjeta = (By.XPATH, '//*[text()="Agregar"]')
    cerrar_form_pago = (By.XPATH, '//div[contains(@class, "payment-picker open")]')
    mensaje_conductor= (By.ID, 'comment')
    boton_manta_panuelo = (By.XPATH, "//div[@class='switch']//span[@class='slider round']")
    agregar_helado = (By.CLASS_NAME, "counter-plus")
    buscar_taxi = (By.CLASS_NAME, 'smart-button')


    def __init__(self, driver):
        self.driver = driver

    def set_from(self, direccion_desde):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(self.campo_desde)
        ).send_keys(direccion_desde)

    def set_to(self, direccion_hasta):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(self.campo_hasta)
        ).send_keys(direccion_hasta)

    def get_from(self):
        return self.driver.find_element(*self.campo_desde).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.campo_hasta).get_property('value')

    def set_route(self, desde_direccion, hasta_direccion ):
        self.set_from(desde_direccion)
        self.set_to(hasta_direccion)

    def get_taxi_button(self):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.boton_pedirtaxi)
        )

    def set_taxi_button(self):
        self.get_taxi_button().click()

    def get_comfort_image(self):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.imagen_comfort)
        )
    def set_comfort_image(self):
        self.get_comfort_image().click()

    def get_number_phone(self):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.boton_numero_telefono)
        )
    def set_number_phone(self):
        self.get_number_phone().click()

    def get_enter_number_phone(self):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.ingresar_numero_telefono)
        )
    def set_enter_number_phone(self,numero_telefono):
        self.get_enter_number_phone().send_keys(numero_telefono)

    def get_next_button(self):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.boton_siguiente)
        )
    def set_next_button(self):
        self.get_next_button().click()

    def get_code_sms(self):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.codigo_sms)
        )
    def set_code_sms(self, codigo):
       self.get_code_sms().send_keys(codigo)

    def get_submit_button(self):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.boton_confirmar)
        )
    def set_submit_button(self):
        self.get_submit_button().click()

    def get_pay_method(self):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.metodo_pago)
        )
    def set_pay_method(self):
        self.get_pay_method().click()

    def get_add_card(self):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.agregar_metodo_pago)
        )
    def set_add_card(self):
        self.get_add_card().click()

    def get_enter_number_card(self):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.ingresa_numero_tarjeta)
        )
    def set_enter_number_card(self, ingresar_numero_tarjeta):
        self.get_enter_number_card().send_keys(ingresar_numero_tarjeta)

    def get_enter_cvv(self):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(self.ingresa_codigo_tarjeta)
        )
    def set_enter_cvv(self, ingresa_codigo_tarjeta):
        cvv= self.get_enter_cvv()
        cvv.send_keys(ingresa_codigo_tarjeta)
        cvv.send_keys(Keys.TAB)

    def get_succes_card(self):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.agregar_tarjeta)
        )
    def set_succes_card(self):
        self.get_succes_card().click()

    def get_button_close_form_pay(self):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.cerrar_form_pago)
        )
    def set_button_close_form_pay(self):
        self.get_button_close_form_pay().click()

    def get_message_driver(self):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.mensaje_conductor)
        )
    def set_message_driver(self,mensajeC):
        self.get_message_driver().send_keys(mensajeC)

    def get_button_round(self):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.boton_manta_panuelo)
        )
    def set_button_round(self):
       button= self.get_button_round()
       self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
       WebDriverWait(self.driver, 3).until(
           expected_conditions.element_to_be_clickable(UrbanRoutesPage.boton_manta_panuelo)
       )
       self.driver.execute_script("arguments[0].click();", button)

    def get_ice_cream(self):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.agregar_helado)
        )

    def set_ice_cream(self):
            agregar_helado = self.get_ice_cream()
            WebDriverWait(self.driver, 10).until(
                expected_conditions.element_to_be_clickable(self.agregar_helado)
            )
            self.driver.execute_script("arguments[0].scrollIntoView(true);", agregar_helado)
            self.driver.execute_script("arguments[0].click();", agregar_helado)
            self.driver.execute_script("arguments[0].click();", agregar_helado)

    def get_search_taxi(self):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.buscar_taxi)
        )
    def set_search_taxi(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(UrbanRoutesPage.buscar_taxi)
        )
        boton_pedir_taxi= self.get_search_taxi()

        self.driver.execute_script("arguments[0].scrollIntoView(true);", boton_pedir_taxi)
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.buscar_taxi)
        )
        self.driver.execute_script("arguments[0].click();", boton_pedir_taxi)


class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        options= Options()
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver=webdriver.Chrome(service=Service(), options=options)

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        direccion_desde = data.address_from
        direccion_hasta = data.address_to
        routes_page.set_route(direccion_desde, direccion_hasta)
        assert routes_page.get_from() == direccion_desde
        assert routes_page.get_to() == direccion_hasta

    def test_boton_pedirtaxi(self):
        self.test_set_route()
        route_page = UrbanRoutesPage(self.driver)
        boton = route_page.get_taxi_button()
        assert boton.is_enabled(), "El botón de pedir taxi no esta habilitado para clic."
        route_page.set_taxi_button()

    def test_imagen_comfort(self):
        self.test_boton_pedirtaxi()
        route_page =UrbanRoutesPage(self.driver)
        route_page.set_comfort_image()
        by,value= UrbanRoutesPage.imagen_comfort
        image= route_page.get_comfort_image().find_element(by,value)
        assert image.is_displayed(), "Error: La tarifa comfort no ha sido seleccionada"

    def test_click_phone_number(self):
        self.test_imagen_comfort()
        route_page = UrbanRoutesPage(self.driver)
        boton_numero = route_page.get_number_phone()
        assert boton_numero.is_enabled(), "No se puede dar click en el telefono"
        route_page.set_number_phone()

    def test_enter_phone_number(self):
        self.test_click_phone_number()
        route_page =UrbanRoutesPage(self.driver)
        numero_telefono= data.phone_number
        route_page.set_enter_number_phone(numero_telefono)
        assert route_page.get_enter_number_phone().get_attribute('value') == data.phone_number

    def test_click_next_button(self):
        self.test_enter_phone_number()
        route_page = UrbanRoutesPage(self.driver)
        route_page.set_next_button()

    def test_code_sms(self):
        self.test_click_next_button()
        route_page =UrbanRoutesPage(self.driver)
        codigo = retrieve_phone_code(self.driver)
        route_page.set_code_sms(codigo)
        input_sms=route_page.get_code_sms().get_attribute('value')
        assert input_sms == codigo, "Error: El codigo SMS no se ingreso o es invalido"

    def test_submit_button(self):
        self.test_code_sms()
        route_page = UrbanRoutesPage(self.driver)
        boton_enviar= route_page.get_submit_button()
        assert boton_enviar.is_enabled(), "enviar"
        route_page.set_submit_button()

    def test_pay_method(self):
        self.test_submit_button()
        route_page = UrbanRoutesPage(self.driver)
        boton_mp = route_page.get_pay_method()
        assert boton_mp.is_enabled(), "No se puede acceder al metodo de pago"
        route_page.set_pay_method()

    def test_add_card(self):
        self.test_pay_method()
        route_page = UrbanRoutesPage(self.driver)
        boton_agregar_tarjeta = route_page.get_add_card()
        assert boton_agregar_tarjeta.is_enabled(), "No se puede agregar tarjeta"
        route_page.set_add_card()


    def test_enter_number_card(self):
        self.test_add_card()
        route_page = UrbanRoutesPage(self.driver)
        ingresar_numero_tarjeta = data.card_number
        route_page.set_enter_number_card(ingresar_numero_tarjeta)
        assert route_page.get_enter_number_card().get_attribute('value') == data.card_number

    def test_enter_code_card(self):
        self.test_enter_number_card()
        route_page = UrbanRoutesPage(self.driver)
        ingresar_codigo_tarjeta = data.card_code
        route_page.set_enter_cvv(ingresar_codigo_tarjeta)
        assert route_page.get_enter_cvv().get_attribute('value') == data.card_code

    def test_card_succes(self):
        self.test_enter_code_card()
        route_page = UrbanRoutesPage(self.driver)
        boton_tarjeta_agregada= route_page.get_succes_card()
        assert boton_tarjeta_agregada.is_enabled(), "La tarjeta no se pudo agregar con exito"
        route_page.set_succes_card()

    def test_button_close_form_pay(self):
        self.test_card_succes()
        route_page = UrbanRoutesPage(self.driver)
        boton_cerrar_mp = route_page.get_button_close_form_pay()
        assert boton_cerrar_mp.is_enabled(), "La ventana de metodo de pago no se pudo cerrar"
        route_page.set_button_close_form_pay()

    def test_message_driver(self):
        self.test_button_close_form_pay()
        route_page = UrbanRoutesPage(self.driver)
        mensajeC = data.message_for_driver
        route_page.set_message_driver(mensajeC)
        assert route_page.get_message_driver().get_attribute('value') == data.message_for_driver

    def test_button_round(self):
        self.test_message_driver()
        route_page = UrbanRoutesPage(self.driver)
        boton_manta= route_page.get_button_round()
        assert boton_manta.is_enabled(), "No se puede agregar las mantas y pañuelos "
        route_page.set_button_round()

    def test_add_ice_cream(self):
        self.test_button_round()
        route_page= UrbanRoutesPage(self.driver)
        boton_helados = route_page.get_ice_cream()
        assert boton_helados.is_enabled(), "Los helados no se pudieron agregar"
        route_page.get_ice_cream()

    def test_search_taxi(self):
        self.test_add_ice_cream()
        route_page = UrbanRoutesPage(self.driver)
        boton_bucar_taxi =route_page.get_search_taxi()
        assert boton_bucar_taxi.is_enabled(), "No se enconto taxi"
        route_page.set_search_taxi()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
