from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from geonature.utils.env import DB
from geonature.utils.utilssqlalchemy import serializable
from pypnnomenclature.models import TNomenclatures



@serializable
class CountingContact(DB.Model):
    __tablename__ = 'cor_counting_contact'
    __table_args__ = {'schema': 'monitoring_chiro'}
    id_counting_contact = DB.Column(DB.Integer, primary_key=True)
    id_contact_taxon = DB.Column(
            DB.Integer,
            ForeignKey('monitoring_chiro.t_visite_contact_taxons.id_contact_taxon')
            )
    id_nomenclature_life_stage = DB.Column(  #Correspondance nomenclature INPN = stade_vie (10)
            DB.Integer,
            ForeignKey(TNomenclatures.id_nomenclature))
    id_nomenclature_sex = DB.Column( #Correspondance nomenclature INPN = sexe (9)
            DB.Integer,
            ForeignKey(TNomenclatures.id_nomenclature))
    id_nomenclature_obj_count = DB.Column(   #Correspondance nomenclature INPN = obj_denbr (6)
            DB.Integer,
            ForeignKey(TNomenclatures.id_nomenclature))
    id_nomenclature_type_count = DB.Column(  #Correspondance nomenclature INPN = typ_denbr (21)
            DB.Integer,
            ForeignKey(TNomenclatures.id_nomenclature))
    count_min = DB.Column(DB.Integer)
    count_max = DB.Column(DB.Integer)
    id_nomenclature_valid_status = DB.Column(   #Correspondance nomenclature INPN = statut_valid (101)
            DB.Integer,
            ForeignKey(TNomenclatures.id_nomenclature))
    id_validator = DB.Column(DB.Integer)
    validation_comment = DB.Column(DB.UnicodeText)
    meta_validation_date = DB.Column(DB.DateTime)
    meta_create_date = DB.Column(DB.DateTime)
    meta_update_date = DB.Column(DB.DateTime)
    unique_id_sinp = DB.Column(UUID(as_uuid=True))