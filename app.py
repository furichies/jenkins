#!/usr/bin/python3
"""
Código de ejemplo reformado con sintaxis correcta de código

"""
from functools import wraps
from flask import Flask, request, jsonify

APP = Flask(__name__)


def check_card(func):
	"""
	Valida datos de trajeta de crédito
	"""
	wraps(func)

	def validation(*args, **kwargs):
		"""
		comentario sobre la funcion
		"""
        	data = request.get_json()
        	if not data.get("status"):
            		response = {"approved": False,
                        "newLimit": data.get("limit"),
                        "reason": "Blocked Card"}
            		return jsonify(response)
        	if data.get("limit") < data.get("transaction").get("amount"):
            		response = {"approved": False,
                        "newLimit": data.get("limit"),
                        "reason": "Transaction above the limit"}
            		return jsonify(response)
            		return func(*args, **kwargs)
	return (validation)


@APP.route("/api/transaction", methods=["POST"])
@check_card
def transaction():
	card = request.get_json()
	new_limit = card.get("limit") - card.get("transaction").get("amount")
	response = {"approved": True, "newLimit": new_limit}
	return jsonify(response)


if __name__ == '__main__':
	APP.run(debug=True)
