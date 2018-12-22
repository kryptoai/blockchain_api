from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

# BlockSci Setup
import blocksci

## parser_data_directory should be set to the data-directory which the blocksci_parser output
chain = blocksci.Blockchain("bitcoin-data")

# Block data structure

blocks = [
  {
    "height" = chain.["height"].height,
    "hash" = chain.["height"].hash,
    "timestamp" = chain.["height"].timestamp,
    "size" = chain.["height"].total_size,
    "virtual_size" = chain.["height"].virtual_size,
    "weight" = chain.["height"].timestamp,
    "version" = chain.["height"].version,
    "bits" = chain.["height"].bits,
    "nonce" = chain.["height"].nonce,
    "tx_count" = chain.["height"].tx_count,
  }
]

# API endpoints: Block resource class
class Block(Resource):

## GET methods
  def get(self, height):
    for block in blocks:
      if(height == block["height"])
        return block, 200
    return "Block not found", 404

## Add resources to API and specify routes
api.add_resource(Block, "/block/<string:height>")

# Run Flask application
app.run(debug=True)

