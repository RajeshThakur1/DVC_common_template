import argparse
import os
import logging
# import config as cfg
STAGE = "STAGE_NAME"

logging.basicConfig(
    filename= os.path.join("logs", "running_log.log"),
    level = logging.INFO,
    format = "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s",
    filemode="a"
)

def main(config_path, params_path):
    pass


if __name__== '__main__':
    BASE_DIR = "D:\Rajesh\My_classes\DVC_implementation\DVC_common_template"
    args = argparse.ArgumentParser()
    args.add_argument("--config", "-c", default= BASE_DIR+ "configs/config.yaml")
    args.add_argument("--params", "-p", default=BASE_DIR + "params.yaml")
    parsed_args =args.parse_args()

    try:
        logging.info("\n****************************")
        logging.info(f">>>>>>>>>>>>>>> Stage {STAGE} started<<<<<<<<<<<<<<<<\n")
        main(config_path=parsed_args.config, params_path=parsed_args.params)
        logging.info(f">>>>>>>>>>>>>>> Stage {STAGE} completed<<<<<<<<<<<<<<<<\n")
    except Exception as e:
        logging.exception(e)
        raise e