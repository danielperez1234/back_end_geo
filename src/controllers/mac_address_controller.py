from models import db, MACAddress

class MACAddressController:
    def add_mac_address(self, mac_address):
        new_mac = MACAddress(mac_address=mac_address)
        db.session.add(new_mac)
        db.session.commit()

    def get_all_mac_addresses(self):
        return MACAddress.query.all()

    def get_mac_address_by_id(self, id):
        return MACAddress.query.get(id)