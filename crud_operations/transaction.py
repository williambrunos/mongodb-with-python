# A transaction is a mongodb operation that has multiple other operators
# that all must perform correctly or cancels all the transactions if there's an error
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
mongodb_uri = os.environ['MONGODB_CONN_STRING']
client = MongoClient(mongodb_uri)

def callback(
        session,
        transfer_id=None,
        account_id_receiver=None,
        account_id_sender=None,
        transfer_amount=None
):
    accounts_collection = session.client.bank.accounts
    transfers_collection = session.client.bank.transfers

    transfer = {
        "transfer_id": transfer_id,
        "account_id_receiver": account_id_receiver,
        "from_account": account_id_sender,
        "ammount": {"$numberDecimal": transfer_amount}
    }

    # IMPORTANT: YOU MUST PASS THE SESSION TO EACH OPERATION
    accounts_collection.update_one(
        {"account_id": account_id_sender},
        {
            "$inc": {"balance": -transfer_amount},
            "$push": {"transfers_complete": transfer_id}
        },
        session=session
    )

    accounts_collection.update_one(
        {"account_id": account_id_receiver},
        {
            "$inc": {"balance": transfer_amount},
            "$push": {"transfers_complete": transfer_id}
        },
        session=session
    )

    transfers_collection.insert_one(transfer, session=session)

    print('Transaction successfully completed!')

    return


def callback_wrapper(session):
    callback(
        session=session,
        transfer_id="123456789",
        account_id_receiver="123456789",
        account_id_sender="123456789",
        transfer_amount=100.00
    )

with client.start_session() as session:
    session.with_transaction(callback_wrapper)

client.close()