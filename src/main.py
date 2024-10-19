from app import app


from indented_logger import IndentedLogger
import logging
logger_setup = IndentedLogger(name='app', level=logging.DEBUG, log_file=None)
logger = logger_setup.get_logger()



if __name__ == "__main__":
    import uvicorn

    # uvicorn.run(app, host="0.0.0.0", port=443, log_level="debug")
    # print("s----------------------------------------------------------------------")
    # print("s----------------------------------------------------------------------")
    # print("s----------------------------------------------------------------------")
    # print("s----------------------------------------------------------------------")

    # uvicorn.run(
    #     "app:app",  # Assuming your FastAPI app is defined in main.py
    #     host="0.0.0.0",
    #     port=443,  # Port 443 for HTTPS
    #     log_level="debug",
    # )

    # Define paths to your SSL certificate and private key


    ssl_certfile = "/home/enes/ssl/combined_certificate.crt"
    ssl_keyfile = "/home/enes/ssl/budgety_ai.key"

    # Run the FastAPI app with SSL on port 443
    uvicorn.run(
        "app:app",  # Assuming your FastAPI app is defined in main.py
        host="0.0.0.0",
        port=443,  # Port 443 for HTTPS
        log_level="debug",
        ssl_certfile=ssl_certfile,  # Path to the SSL certificate
        ssl_keyfile=ssl_keyfile     # Path to the SSL private key
    )



