# Proyecto Lambda Example

Este proyecto contiene dos funciones Lambda de AWS: `WebhookFunction` y `WorkerFunction`. La `WebhookFunction` recibe mensajes HTTP POST y los guarda en una base de datos MySQL. La `WorkerFunction` procesa mensajes de una cola SQS y actualiza el estado de los mensajes en la base de datos.

## Estructura del Proyecto

- `webhook/`: Contiene el código para la función `WebhookFunction`.
- `worker/`: Contiene el código para la función `WorkerFunction`.
- `template.yaml`: Plantilla de AWS SAM para desplegar las funciones Lambda y otros recursos.
- `requirements.txt`: Lista de dependencias de Python.
- `.gitignore`: Archivos y carpetas a ignorar por Git.
- `venv/`: Entorno virtual de Python.

## Dependencias

Las dependencias del proyecto están listadas en el archivo `requirements.txt`:

```
boto3==1.36.3
botocore==1.36.3
jmespath==1.0.1
PyMySQL==1.1.1
python-dateutil==2.9.0.post0
s3transfer==0.11.1
six==1.17.0
urllib3==2.3.0
```

## Configuración del Entorno

1. Crear un entorno virtual:

   ```bash
   python -m venv venv
   ```

2. Activar el entorno virtual:

   - En Windows:

     ```bash
     venv\Scripts\activate
     ```

   - En macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

3. Instalar las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

## Despliegue

Para desplegar las funciones Lambda y otros recursos, utilizar AWS SAM CLI:

```bash
sam deploy --guided
```

Seguir las instrucciones en pantalla para configurar el despliegue.

## Ejecución Local

Para probar las funciones Lambda localmente, utilizar AWS SAM CLI:

- Ejecutar `WebhookFunction` localmente:

  ```bash
  sam local invoke WebhookFunction --event events/webhook_event.json
  ```

- Ejecutar `WorkerFunction` localmente:

  ```bash
  sam local invoke WorkerFunction --event events/worker_event.json
  ```

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abrir un issue o enviar un pull request para discutir cualquier cambio.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.
