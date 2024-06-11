# fixture
En pytest, @pytest.fixture se utiliza para definir una función de fixture. Un fixture es una función que se ejecuta antes de cada prueba y proporciona datos o realiza configuraciones necesarias para la prueba.
Aquí tienes un ejemplo de cómo se utiliza @pytest.fixture:

```
import pytest

@pytest.fixture
def setup_data():
    # Configuración inicial de datos
    data = [1, 2, 3, 4, 5]
    return data

def test_example(setup_data):
    # Utilizando el fixture setup_data en la prueba
    assert len(setup_data) == 5
```

En este ejemplo, `setup_data` es una función de fixture que se ejecutará antes de cada prueba que lo utilice. En la función `setup_data, puedes realizar cualquier configuración necesaria, como cargar datos desde una base de datos o preparar objetos para la prueba.

En la prueba `test_example`, se utiliza el fixture `setup_data` como un argumento de la función de prueba. Esto permite acceder a los datos o configuraciones proporcionados por el fixture dentro de la prueba. En este caso, estamos verificando que la longitud de los datos proporcionados por el fixture sea igual a 5.

Los fixtures son útiles cuando necesitas realizar tareas repetitivas de configuración antes de cada prueba, como inicializar objetos o cargar datos. Al utilizar fixtures, puedes mantener tu código de prueba más limpio y modular, ya que puedes reutilizar la configuración en varias pruebas.
