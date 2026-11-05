# Auto generated from iso29100.yaml by pythongen.py version: 0.0.1
# Schema: iso29100
#
# id: https://w3id.org/lmodel/iso29100
# description: A LinkML model of the records an organization keeps when it applies the privacy framework of ISO/IEC 29100:2024 to the information and communication technology (ICT) systems that handle personally identifiable information (PII). The records say who takes part, which PII is involved and how it moves, what must be safeguarded and how, and how the organization stands against each privacy principle.
# license: Apache-2.0

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Boolean, Date, Datetime, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, URIorCURIE, XSDDate, XSDDateTime

metamodel_version = "1.12.0"
version = "2024"

# Namespaces
DPV = CurieNamespace('dpv', 'https://w3id.org/dpv#')
ISO29100 = CurieNamespace('iso29100', 'https://w3id.org/lmodel/iso29100/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = ISO29100


# Types
class PfDuration(String):
    """ A length of time as ISO 8601 writes it, such as P7Y for seven years or P30D for thirty days. """
    type_class_uri = XSD["duration"]
    type_class_curie = "xsd:duration"
    type_name = "pf_duration"
    type_model_uri = ISO29100.PfDuration


# Class references
class PfRecordMixinPfId(URIorCURIE):
    pass


class PfFrameworkPfId(URIorCURIE):
    pass


class PfActorPfId(URIorCURIE):
    pass


class PfPiiPrincipalPfId(PfActorPfId):
    pass


class PfPiiControllerPfId(PfActorPfId):
    pass


class PfPiiProcessorPfId(PfActorPfId):
    pass


class PfThirdPartyPfId(PfActorPfId):
    pass


class PfPiiItemPfId(URIorCURIE):
    pass


class PfPiiFlowPfId(URIorCURIE):
    pass


class PfProcessingActivityPfId(URIorCURIE):
    pass


class PfSafeguardingRequirementPfId(URIorCURIE):
    pass


class PfPolicyPfId(URIorCURIE):
    pass


class PfControlPfId(URIorCURIE):
    pass


class PfPrincipleImplementationPfId(URIorCURIE):
    pass


class PfRiskPfId(URIorCURIE):
    pass


class PfImpactAssessmentPfId(URIorCURIE):
    pass


class PfBreachPfId(URIorCURIE):
    pass


class PfConsentPfId(URIorCURIE):
    pass


class PfPreferencePfId(URIorCURIE):
    pass


@dataclass(repr=False)
class PfRecordMixin(YAMLRoot):
    """
    What every record of the framework has, so that other records can refer to it: an identifier, a title and a
    description.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO29100["PfRecordMixin"]
    class_class_curie: ClassVar[str] = "iso29100:PfRecordMixin"
    class_name: ClassVar[str] = "PfRecordMixin"
    class_model_uri: ClassVar[URIRef] = ISO29100.PfRecordMixin

    pf_id: Union[str, PfRecordMixinPfId] = None
    title: str = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.pf_id):
            self.MissingRequiredField("pf_id")
        if not isinstance(self.pf_id, PfRecordMixinPfId):
            self.pf_id = PfRecordMixinPfId(self.pf_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PfFramework(YAMLRoot):
    """
    One organization's use of the privacy framework: the systems it covers, and every record the organization keeps
    about them, each kind in a list of its own.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO29100["PfFramework"]
    class_class_curie: ClassVar[str] = "iso29100:PfFramework"
    class_name: ClassVar[str] = "PfFramework"
    class_model_uri: ClassVar[URIRef] = ISO29100.PfFramework

    pf_id: Union[str, PfFrameworkPfId] = None
    pf_organization: str = None
    title: str = None
    pf_jurisdictions: Optional[Union[str, list[str]]] = empty_list()
    pf_ict_systems: Optional[Union[str, list[str]]] = empty_list()
    pf_actors: Optional[Union[dict[Union[str, PfActorPfId], Union[dict, "PfActor"]], list[Union[dict, "PfActor"]]]] = empty_dict()
    pf_pii_items: Optional[Union[dict[Union[str, PfPiiItemPfId], Union[dict, "PfPiiItem"]], list[Union[dict, "PfPiiItem"]]]] = empty_dict()
    pf_flows: Optional[Union[dict[Union[str, PfPiiFlowPfId], Union[dict, "PfPiiFlow"]], list[Union[dict, "PfPiiFlow"]]]] = empty_dict()
    pf_processing_activities: Optional[Union[dict[Union[str, PfProcessingActivityPfId], Union[dict, "PfProcessingActivity"]], list[Union[dict, "PfProcessingActivity"]]]] = empty_dict()
    pf_safeguarding_requirements: Optional[Union[dict[Union[str, PfSafeguardingRequirementPfId], Union[dict, "PfSafeguardingRequirement"]], list[Union[dict, "PfSafeguardingRequirement"]]]] = empty_dict()
    pf_policies: Optional[Union[dict[Union[str, PfPolicyPfId], Union[dict, "PfPolicy"]], list[Union[dict, "PfPolicy"]]]] = empty_dict()
    pf_controls: Optional[Union[dict[Union[str, PfControlPfId], Union[dict, "PfControl"]], list[Union[dict, "PfControl"]]]] = empty_dict()
    pf_principle_implementations: Optional[Union[dict[Union[str, PfPrincipleImplementationPfId], Union[dict, "PfPrincipleImplementation"]], list[Union[dict, "PfPrincipleImplementation"]]]] = empty_dict()
    pf_risks: Optional[Union[dict[Union[str, PfRiskPfId], Union[dict, "PfRisk"]], list[Union[dict, "PfRisk"]]]] = empty_dict()
    pf_impact_assessments: Optional[Union[dict[Union[str, PfImpactAssessmentPfId], Union[dict, "PfImpactAssessment"]], list[Union[dict, "PfImpactAssessment"]]]] = empty_dict()
    pf_breaches: Optional[Union[dict[Union[str, PfBreachPfId], Union[dict, "PfBreach"]], list[Union[dict, "PfBreach"]]]] = empty_dict()
    pf_consents: Optional[Union[dict[Union[str, PfConsentPfId], Union[dict, "PfConsent"]], list[Union[dict, "PfConsent"]]]] = empty_dict()
    pf_preferences: Optional[Union[dict[Union[str, PfPreferencePfId], Union[dict, "PfPreference"]], list[Union[dict, "PfPreference"]]]] = empty_dict()
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.pf_id):
            self.MissingRequiredField("pf_id")
        if not isinstance(self.pf_id, PfFrameworkPfId):
            self.pf_id = PfFrameworkPfId(self.pf_id)

        if self._is_empty(self.pf_organization):
            self.MissingRequiredField("pf_organization")
        if not isinstance(self.pf_organization, str):
            self.pf_organization = str(self.pf_organization)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.pf_jurisdictions, list):
            self.pf_jurisdictions = [self.pf_jurisdictions] if self.pf_jurisdictions is not None else []
        self.pf_jurisdictions = [v if isinstance(v, str) else str(v) for v in self.pf_jurisdictions]

        if not isinstance(self.pf_ict_systems, list):
            self.pf_ict_systems = [self.pf_ict_systems] if self.pf_ict_systems is not None else []
        self.pf_ict_systems = [v if isinstance(v, str) else str(v) for v in self.pf_ict_systems]

        self._normalize_inlined_as_list(slot_name="pf_actors", slot_type=PfActor, key_name="pf_id", keyed=True)

        self._normalize_inlined_as_list(slot_name="pf_pii_items", slot_type=PfPiiItem, key_name="pf_id", keyed=True)

        self._normalize_inlined_as_list(slot_name="pf_flows", slot_type=PfPiiFlow, key_name="pf_id", keyed=True)

        self._normalize_inlined_as_list(slot_name="pf_processing_activities", slot_type=PfProcessingActivity, key_name="pf_id", keyed=True)

        self._normalize_inlined_as_list(slot_name="pf_safeguarding_requirements", slot_type=PfSafeguardingRequirement, key_name="pf_id", keyed=True)

        self._normalize_inlined_as_list(slot_name="pf_policies", slot_type=PfPolicy, key_name="pf_id", keyed=True)

        self._normalize_inlined_as_list(slot_name="pf_controls", slot_type=PfControl, key_name="pf_id", keyed=True)

        self._normalize_inlined_as_list(slot_name="pf_principle_implementations", slot_type=PfPrincipleImplementation, key_name="pf_id", keyed=True)

        self._normalize_inlined_as_list(slot_name="pf_risks", slot_type=PfRisk, key_name="pf_id", keyed=True)

        self._normalize_inlined_as_list(slot_name="pf_impact_assessments", slot_type=PfImpactAssessment, key_name="pf_id", keyed=True)

        self._normalize_inlined_as_list(slot_name="pf_breaches", slot_type=PfBreach, key_name="pf_id", keyed=True)

        self._normalize_inlined_as_list(slot_name="pf_consents", slot_type=PfConsent, key_name="pf_id", keyed=True)

        self._normalize_inlined_as_list(slot_name="pf_preferences", slot_type=PfPreference, key_name="pf_id", keyed=True)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PfActor(YAMLRoot):
    """
    Someone who takes part in handling PII, told apart by the part they play. One party can play different parts for
    different PII, with a record for each.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO29100["PfActor"]
    class_class_curie: ClassVar[str] = "iso29100:PfActor"
    class_name: ClassVar[str] = "PfActor"
    class_model_uri: ClassVar[URIRef] = ISO29100.PfActor

    pf_id: Union[str, PfActorPfId] = None
    pf_actor_type: str = None
    title: str = None
    pf_jurisdictions: Optional[Union[str, list[str]]] = empty_list()
    pf_contact: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.pf_actor_type):
            self.MissingRequiredField("pf_actor_type")
        self.pf_actor_type = str(self.class_name)

        if self._is_empty(self.pf_id):
            self.MissingRequiredField("pf_id")
        if not isinstance(self.pf_id, PfActorPfId):
            self.pf_id = PfActorPfId(self.pf_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.pf_jurisdictions, list):
            self.pf_jurisdictions = [self.pf_jurisdictions] if self.pf_jurisdictions is not None else []
        self.pf_jurisdictions = [v if isinstance(v, str) else str(v) for v in self.pf_jurisdictions]

        if self.pf_contact is not None and not isinstance(self.pf_contact, str):
            self.pf_contact = str(self.pf_contact)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)
        if self._is_empty(self.pf_actor_type):
            self.MissingRequiredField("pf_actor_type")
        self.pf_actor_type = str(self.class_name)


    def __new__(cls, *args, **kwargs):

        type_designator = "pf_actor_type"
        if not type_designator in kwargs:
            return super().__new__(cls,*args,**kwargs)
        else:
            type_designator_value = kwargs[type_designator]
            target_cls = cls._class_for("class_name", type_designator_value)


            if target_cls is None:
                raise ValueError(f"Wrong type designator value: class {cls.__name__} "
                                 f"has no subclass with ['class_name']='{kwargs[type_designator]}'")
            return super().__new__(target_cls,*args,**kwargs)



@dataclass(repr=False)
class PfPiiPrincipal(PfActor):
    """
    The person the PII is about, or a group of such people when the organization records them together.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO29100["PfPiiPrincipal"]
    class_class_curie: ClassVar[str] = "iso29100:PfPiiPrincipal"
    class_name: ClassVar[str] = "PfPiiPrincipal"
    class_model_uri: ClassVar[URIRef] = ISO29100.PfPiiPrincipal

    pf_id: Union[str, PfPiiPrincipalPfId] = None
    pf_actor_type: str = None
    title: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.pf_id):
            self.MissingRequiredField("pf_id")
        if not isinstance(self.pf_id, PfPiiPrincipalPfId):
            self.pf_id = PfPiiPrincipalPfId(self.pf_id)

        super().__post_init__(**kwargs)
        if self._is_empty(self.pf_actor_type):
            self.MissingRequiredField("pf_actor_type")
        self.pf_actor_type = str(self.class_name)


@dataclass(repr=False)
class PfPiiController(PfActor):
    """
    The party that decides why and how PII is processed, and answers for it even when another party does the work.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO29100["PfPiiController"]
    class_class_curie: ClassVar[str] = "iso29100:PfPiiController"
    class_name: ClassVar[str] = "PfPiiController"
    class_model_uri: ClassVar[URIRef] = ISO29100.PfPiiController

    pf_id: Union[str, PfPiiControllerPfId] = None
    pf_actor_type: str = None
    title: str = None
    pf_purposes: Optional[Union[str, list[str]]] = empty_list()
    pf_legal_bases: Optional[Union[str, list[str]]] = empty_list()
    pf_appointed_processors: Optional[Union[Union[str, PfPiiProcessorPfId], list[Union[str, PfPiiProcessorPfId]]]] = empty_list()
    pf_controller_policy: Optional[Union[str, PfPolicyPfId]] = None
    pf_privacy_officer: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.pf_id):
            self.MissingRequiredField("pf_id")
        if not isinstance(self.pf_id, PfPiiControllerPfId):
            self.pf_id = PfPiiControllerPfId(self.pf_id)

        if not isinstance(self.pf_purposes, list):
            self.pf_purposes = [self.pf_purposes] if self.pf_purposes is not None else []
        self.pf_purposes = [v if isinstance(v, str) else str(v) for v in self.pf_purposes]

        if not isinstance(self.pf_legal_bases, list):
            self.pf_legal_bases = [self.pf_legal_bases] if self.pf_legal_bases is not None else []
        self.pf_legal_bases = [v if isinstance(v, str) else str(v) for v in self.pf_legal_bases]

        if not isinstance(self.pf_appointed_processors, list):
            self.pf_appointed_processors = [self.pf_appointed_processors] if self.pf_appointed_processors is not None else []
        self.pf_appointed_processors = [v if isinstance(v, PfPiiProcessorPfId) else PfPiiProcessorPfId(v) for v in self.pf_appointed_processors]

        if self.pf_controller_policy is not None and not isinstance(self.pf_controller_policy, PfPolicyPfId):
            self.pf_controller_policy = PfPolicyPfId(self.pf_controller_policy)

        if self.pf_privacy_officer is not None and not isinstance(self.pf_privacy_officer, str):
            self.pf_privacy_officer = str(self.pf_privacy_officer)

        super().__post_init__(**kwargs)
        if self._is_empty(self.pf_actor_type):
            self.MissingRequiredField("pf_actor_type")
        self.pf_actor_type = str(self.class_name)


@dataclass(repr=False)
class PfPiiProcessor(PfActor):
    """
    A party that processes PII for a controller, on that controller's instructions.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO29100["PfPiiProcessor"]
    class_class_curie: ClassVar[str] = "iso29100:PfPiiProcessor"
    class_name: ClassVar[str] = "PfPiiProcessor"
    class_model_uri: ClassVar[URIRef] = ISO29100.PfPiiProcessor

    pf_id: Union[str, PfPiiProcessorPfId] = None
    pf_actor_type: str = None
    title: str = None
    pf_instructing_controllers: Optional[Union[Union[str, PfPiiControllerPfId], list[Union[str, PfPiiControllerPfId]]]] = empty_list()
    pf_processing_agreement: Optional[str] = None
    pf_sub_processors: Optional[Union[Union[str, PfPiiProcessorPfId], list[Union[str, PfPiiProcessorPfId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.pf_id):
            self.MissingRequiredField("pf_id")
        if not isinstance(self.pf_id, PfPiiProcessorPfId):
            self.pf_id = PfPiiProcessorPfId(self.pf_id)

        if not isinstance(self.pf_instructing_controllers, list):
            self.pf_instructing_controllers = [self.pf_instructing_controllers] if self.pf_instructing_controllers is not None else []
        self.pf_instructing_controllers = [v if isinstance(v, PfPiiControllerPfId) else PfPiiControllerPfId(v) for v in self.pf_instructing_controllers]

        if self.pf_processing_agreement is not None and not isinstance(self.pf_processing_agreement, str):
            self.pf_processing_agreement = str(self.pf_processing_agreement)

        if not isinstance(self.pf_sub_processors, list):
            self.pf_sub_processors = [self.pf_sub_processors] if self.pf_sub_processors is not None else []
        self.pf_sub_processors = [v if isinstance(v, PfPiiProcessorPfId) else PfPiiProcessorPfId(v) for v in self.pf_sub_processors]

        super().__post_init__(**kwargs)
        if self._is_empty(self.pf_actor_type):
            self.MissingRequiredField("pf_actor_type")
        self.pf_actor_type = str(self.class_name)


@dataclass(repr=False)
class PfThirdParty(PfActor):
    """
    A party outside the controller and its processors that receives PII for its own ends, and usually becomes a
    controller of that PII.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO29100["PfThirdParty"]
    class_class_curie: ClassVar[str] = "iso29100:PfThirdParty"
    class_name: ClassVar[str] = "PfThirdParty"
    class_model_uri: ClassVar[URIRef] = ISO29100.PfThirdParty

    pf_id: Union[str, PfThirdPartyPfId] = None
    pf_actor_type: str = None
    title: str = None
    pf_receiving_purpose: Optional[str] = None
    pf_transfer_basis: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.pf_id):
            self.MissingRequiredField("pf_id")
        if not isinstance(self.pf_id, PfThirdPartyPfId):
            self.pf_id = PfThirdPartyPfId(self.pf_id)

        if self.pf_receiving_purpose is not None and not isinstance(self.pf_receiving_purpose, str):
            self.pf_receiving_purpose = str(self.pf_receiving_purpose)

        if self.pf_transfer_basis is not None and not isinstance(self.pf_transfer_basis, str):
            self.pf_transfer_basis = str(self.pf_transfer_basis)

        super().__post_init__(**kwargs)
        if self._is_empty(self.pf_actor_type):
            self.MissingRequiredField("pf_actor_type")
        self.pf_actor_type = str(self.class_name)


@dataclass(repr=False)
class PfPiiItem(YAMLRoot):
    """
    A piece or set of information that can be tied to a person, why it counts as PII, how sensitive it is and how it
    is handled.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO29100["PfPiiItem"]
    class_class_curie: ClassVar[str] = "iso29100:PfPiiItem"
    class_name: ClassVar[str] = "PfPiiItem"
    class_model_uri: ClassVar[URIRef] = ISO29100.PfPiiItem

    pf_id: Union[str, PfPiiItemPfId] = None
    title: str = None
    pf_concerned_principals: Optional[Union[Union[str, PfPiiPrincipalPfId], list[Union[str, PfPiiPrincipalPfId]]]] = empty_list()
    pf_operations: Optional[Union[Union[str, "PfOperation"], list[Union[str, "PfOperation"]]]] = empty_list()
    pf_retention: Optional[Union[str, PfDuration]] = None
    pf_pii_categories: Optional[Union[str, list[str]]] = empty_list()
    pf_recognized_by: Optional[Union[Union[str, "PfPiiRecognition"], list[Union[str, "PfPiiRecognition"]]]] = empty_list()
    pf_sensitivity: Optional[Union[str, "PfSensitivity"]] = None
    pf_pseudonymized: Optional[Union[bool, Bool]] = None
    pf_linkability: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.pf_id):
            self.MissingRequiredField("pf_id")
        if not isinstance(self.pf_id, PfPiiItemPfId):
            self.pf_id = PfPiiItemPfId(self.pf_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.pf_concerned_principals, list):
            self.pf_concerned_principals = [self.pf_concerned_principals] if self.pf_concerned_principals is not None else []
        self.pf_concerned_principals = [v if isinstance(v, PfPiiPrincipalPfId) else PfPiiPrincipalPfId(v) for v in self.pf_concerned_principals]

        if not isinstance(self.pf_operations, list):
            self.pf_operations = [self.pf_operations] if self.pf_operations is not None else []
        self.pf_operations = [v if isinstance(v, PfOperation) else PfOperation(v) for v in self.pf_operations]

        if self.pf_retention is not None and not isinstance(self.pf_retention, PfDuration):
            self.pf_retention = PfDuration(self.pf_retention)

        if not isinstance(self.pf_pii_categories, list):
            self.pf_pii_categories = [self.pf_pii_categories] if self.pf_pii_categories is not None else []
        self.pf_pii_categories = [v if isinstance(v, str) else str(v) for v in self.pf_pii_categories]

        if not isinstance(self.pf_recognized_by, list):
            self.pf_recognized_by = [self.pf_recognized_by] if self.pf_recognized_by is not None else []
        self.pf_recognized_by = [v if isinstance(v, PfPiiRecognition) else PfPiiRecognition(v) for v in self.pf_recognized_by]

        if self.pf_sensitivity is not None and not isinstance(self.pf_sensitivity, PfSensitivity):
            self.pf_sensitivity = PfSensitivity(self.pf_sensitivity)

        if self.pf_pseudonymized is not None and not isinstance(self.pf_pseudonymized, Bool):
            self.pf_pseudonymized = Bool(self.pf_pseudonymized)

        if self.pf_linkability is not None and not isinstance(self.pf_linkability, str):
            self.pf_linkability = str(self.pf_linkability)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PfPiiFlow(YAMLRoot):
    """
    One way PII passes from one actor to another, and who decides what happens to it afterwards.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO29100["PfPiiFlow"]
    class_class_curie: ClassVar[str] = "iso29100:PfPiiFlow"
    class_name: ClassVar[str] = "PfPiiFlow"
    class_model_uri: ClassVar[URIRef] = ISO29100.PfPiiFlow

    pf_id: Union[str, PfPiiFlowPfId] = None
    pf_provider: Union[str, PfActorPfId] = None
    pf_recipient: Union[str, PfActorPfId] = None
    title: str = None
    pf_concerned_pii: Optional[Union[Union[str, PfPiiItemPfId], list[Union[str, PfPiiItemPfId]]]] = empty_list()
    pf_decides_afterwards: Optional[Union[str, PfActorPfId]] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.pf_id):
            self.MissingRequiredField("pf_id")
        if not isinstance(self.pf_id, PfPiiFlowPfId):
            self.pf_id = PfPiiFlowPfId(self.pf_id)

        if self._is_empty(self.pf_provider):
            self.MissingRequiredField("pf_provider")
        if not isinstance(self.pf_provider, PfActorPfId):
            self.pf_provider = PfActorPfId(self.pf_provider)

        if self._is_empty(self.pf_recipient):
            self.MissingRequiredField("pf_recipient")
        if not isinstance(self.pf_recipient, PfActorPfId):
            self.pf_recipient = PfActorPfId(self.pf_recipient)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.pf_concerned_pii, list):
            self.pf_concerned_pii = [self.pf_concerned_pii] if self.pf_concerned_pii is not None else []
        self.pf_concerned_pii = [v if isinstance(v, PfPiiItemPfId) else PfPiiItemPfId(v) for v in self.pf_concerned_pii]

        if self.pf_decides_afterwards is not None and not isinstance(self.pf_decides_afterwards, PfActorPfId):
            self.pf_decides_afterwards = PfActorPfId(self.pf_decides_afterwards)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PfProcessingActivity(YAMLRoot):
    """
    Something the organization does with PII: why, on what basis, what it does to which PII, who is responsible, and
    how long the PII is kept.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO29100["PfProcessingActivity"]
    class_class_curie: ClassVar[str] = "iso29100:PfProcessingActivity"
    class_name: ClassVar[str] = "PfProcessingActivity"
    class_model_uri: ClassVar[URIRef] = ISO29100.PfProcessingActivity

    pf_id: Union[str, PfProcessingActivityPfId] = None
    pf_controller: Union[str, PfPiiControllerPfId] = None
    title: str = None
    pf_purposes: Optional[Union[str, list[str]]] = empty_list()
    pf_legal_bases: Optional[Union[str, list[str]]] = empty_list()
    pf_operations: Optional[Union[Union[str, "PfOperation"], list[Union[str, "PfOperation"]]]] = empty_list()
    pf_concerned_pii: Optional[Union[Union[str, PfPiiItemPfId], list[Union[str, PfPiiItemPfId]]]] = empty_list()
    pf_retention: Optional[Union[str, PfDuration]] = None
    pf_related_controls: Optional[Union[Union[str, PfControlPfId], list[Union[str, PfControlPfId]]]] = empty_list()
    pf_processors: Optional[Union[Union[str, PfPiiProcessorPfId], list[Union[str, PfPiiProcessorPfId]]]] = empty_list()
    pf_activity_flows: Optional[Union[Union[str, PfPiiFlowPfId], list[Union[str, PfPiiFlowPfId]]]] = empty_list()
    pf_sensitivities: Optional[Union[Union[str, "PfSensitivity"], list[Union[str, "PfSensitivity"]]]] = empty_list()
    pf_crosses_borders: Optional[Union[bool, Bool]] = None
    pf_transfer_safeguards: Optional[Union[str, list[str]]] = empty_list()
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.pf_id):
            self.MissingRequiredField("pf_id")
        if not isinstance(self.pf_id, PfProcessingActivityPfId):
            self.pf_id = PfProcessingActivityPfId(self.pf_id)

        if self._is_empty(self.pf_controller):
            self.MissingRequiredField("pf_controller")
        if not isinstance(self.pf_controller, PfPiiControllerPfId):
            self.pf_controller = PfPiiControllerPfId(self.pf_controller)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.pf_purposes, list):
            self.pf_purposes = [self.pf_purposes] if self.pf_purposes is not None else []
        self.pf_purposes = [v if isinstance(v, str) else str(v) for v in self.pf_purposes]

        if not isinstance(self.pf_legal_bases, list):
            self.pf_legal_bases = [self.pf_legal_bases] if self.pf_legal_bases is not None else []
        self.pf_legal_bases = [v if isinstance(v, str) else str(v) for v in self.pf_legal_bases]

        if not isinstance(self.pf_operations, list):
            self.pf_operations = [self.pf_operations] if self.pf_operations is not None else []
        self.pf_operations = [v if isinstance(v, PfOperation) else PfOperation(v) for v in self.pf_operations]

        if not isinstance(self.pf_concerned_pii, list):
            self.pf_concerned_pii = [self.pf_concerned_pii] if self.pf_concerned_pii is not None else []
        self.pf_concerned_pii = [v if isinstance(v, PfPiiItemPfId) else PfPiiItemPfId(v) for v in self.pf_concerned_pii]

        if self.pf_retention is not None and not isinstance(self.pf_retention, PfDuration):
            self.pf_retention = PfDuration(self.pf_retention)

        if not isinstance(self.pf_related_controls, list):
            self.pf_related_controls = [self.pf_related_controls] if self.pf_related_controls is not None else []
        self.pf_related_controls = [v if isinstance(v, PfControlPfId) else PfControlPfId(v) for v in self.pf_related_controls]

        if not isinstance(self.pf_processors, list):
            self.pf_processors = [self.pf_processors] if self.pf_processors is not None else []
        self.pf_processors = [v if isinstance(v, PfPiiProcessorPfId) else PfPiiProcessorPfId(v) for v in self.pf_processors]

        if not isinstance(self.pf_activity_flows, list):
            self.pf_activity_flows = [self.pf_activity_flows] if self.pf_activity_flows is not None else []
        self.pf_activity_flows = [v if isinstance(v, PfPiiFlowPfId) else PfPiiFlowPfId(v) for v in self.pf_activity_flows]

        if not isinstance(self.pf_sensitivities, list):
            self.pf_sensitivities = [self.pf_sensitivities] if self.pf_sensitivities is not None else []
        self.pf_sensitivities = [v if isinstance(v, PfSensitivity) else PfSensitivity(v) for v in self.pf_sensitivities]

        if self.pf_crosses_borders is not None and not isinstance(self.pf_crosses_borders, Bool):
            self.pf_crosses_borders = Bool(self.pf_crosses_borders)

        if not isinstance(self.pf_transfer_safeguards, list):
            self.pf_transfer_safeguards = [self.pf_transfer_safeguards] if self.pf_transfer_safeguards is not None else []
        self.pf_transfer_safeguards = [v if isinstance(v, str) else str(v) for v in self.pf_transfer_safeguards]

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PfSafeguardingRequirement(YAMLRoot):
    """
    Something the organization must do to protect PII, and where that duty comes from.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO29100["PfSafeguardingRequirement"]
    class_class_curie: ClassVar[str] = "iso29100:PfSafeguardingRequirement"
    class_name: ClassVar[str] = "PfSafeguardingRequirement"
    class_model_uri: ClassVar[URIRef] = ISO29100.PfSafeguardingRequirement

    pf_id: Union[str, PfSafeguardingRequirementPfId] = None
    pf_requirement_factor: Union[str, "PfRequirementFactor"] = None
    title: str = None
    pf_requirement_source: Optional[str] = None
    pf_applies_to: Optional[Union[Union[str, PfActorPfId], list[Union[str, PfActorPfId]]]] = empty_list()
    pf_met_by: Optional[Union[Union[str, PfControlPfId], list[Union[str, PfControlPfId]]]] = empty_list()
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.pf_id):
            self.MissingRequiredField("pf_id")
        if not isinstance(self.pf_id, PfSafeguardingRequirementPfId):
            self.pf_id = PfSafeguardingRequirementPfId(self.pf_id)

        if self._is_empty(self.pf_requirement_factor):
            self.MissingRequiredField("pf_requirement_factor")
        if not isinstance(self.pf_requirement_factor, PfRequirementFactor):
            self.pf_requirement_factor = PfRequirementFactor(self.pf_requirement_factor)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self.pf_requirement_source is not None and not isinstance(self.pf_requirement_source, str):
            self.pf_requirement_source = str(self.pf_requirement_source)

        if not isinstance(self.pf_applies_to, list):
            self.pf_applies_to = [self.pf_applies_to] if self.pf_applies_to is not None else []
        self.pf_applies_to = [v if isinstance(v, PfActorPfId) else PfActorPfId(v) for v in self.pf_applies_to]

        if not isinstance(self.pf_met_by, list):
            self.pf_met_by = [self.pf_met_by] if self.pf_met_by is not None else []
        self.pf_met_by = [v if isinstance(v, PfControlPfId) else PfControlPfId(v) for v in self.pf_met_by]

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PfPolicy(YAMLRoot):
    """
    A privacy policy: what the organization commits to about PII, written for its own people or as a notice to the
    people whose PII it handles.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO29100["PfPolicy"]
    class_class_curie: ClassVar[str] = "iso29100:PfPolicy"
    class_name: ClassVar[str] = "PfPolicy"
    class_model_uri: ClassVar[URIRef] = ISO29100.PfPolicy

    pf_id: Union[str, PfPolicyPfId] = None
    pf_policy_audience: Union[str, "PfPolicyAudience"] = None
    title: str = None
    pf_purposes: Optional[Union[str, list[str]]] = empty_list()
    pf_concerned_pii: Optional[Union[Union[str, PfPiiItemPfId], list[Union[str, PfPiiItemPfId]]]] = empty_list()
    pf_principles: Optional[Union[Union[str, "PfPrinciple"], list[Union[str, "PfPrinciple"]]]] = empty_list()
    pf_policy_version: Optional[str] = None
    pf_policy_scope: Optional[str] = None
    pf_policy_effective_date: Optional[Union[str, XSDDate]] = None
    pf_policy_last_reviewed: Optional[Union[str, XSDDate]] = None
    pf_retention_statement: Optional[str] = None
    pf_stated_rights: Optional[Union[str, list[str]]] = empty_list()
    pf_inquiry_contact: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.pf_id):
            self.MissingRequiredField("pf_id")
        if not isinstance(self.pf_id, PfPolicyPfId):
            self.pf_id = PfPolicyPfId(self.pf_id)

        if self._is_empty(self.pf_policy_audience):
            self.MissingRequiredField("pf_policy_audience")
        if not isinstance(self.pf_policy_audience, PfPolicyAudience):
            self.pf_policy_audience = PfPolicyAudience(self.pf_policy_audience)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.pf_purposes, list):
            self.pf_purposes = [self.pf_purposes] if self.pf_purposes is not None else []
        self.pf_purposes = [v if isinstance(v, str) else str(v) for v in self.pf_purposes]

        if not isinstance(self.pf_concerned_pii, list):
            self.pf_concerned_pii = [self.pf_concerned_pii] if self.pf_concerned_pii is not None else []
        self.pf_concerned_pii = [v if isinstance(v, PfPiiItemPfId) else PfPiiItemPfId(v) for v in self.pf_concerned_pii]

        if not isinstance(self.pf_principles, list):
            self.pf_principles = [self.pf_principles] if self.pf_principles is not None else []
        self.pf_principles = [v if isinstance(v, PfPrinciple) else PfPrinciple(v) for v in self.pf_principles]

        if self.pf_policy_version is not None and not isinstance(self.pf_policy_version, str):
            self.pf_policy_version = str(self.pf_policy_version)

        if self.pf_policy_scope is not None and not isinstance(self.pf_policy_scope, str):
            self.pf_policy_scope = str(self.pf_policy_scope)

        if self.pf_policy_effective_date is not None and not isinstance(self.pf_policy_effective_date, XSDDate):
            self.pf_policy_effective_date = XSDDate(self.pf_policy_effective_date)

        if self.pf_policy_last_reviewed is not None and not isinstance(self.pf_policy_last_reviewed, XSDDate):
            self.pf_policy_last_reviewed = XSDDate(self.pf_policy_last_reviewed)

        if self.pf_retention_statement is not None and not isinstance(self.pf_retention_statement, str):
            self.pf_retention_statement = str(self.pf_retention_statement)

        if not isinstance(self.pf_stated_rights, list):
            self.pf_stated_rights = [self.pf_stated_rights] if self.pf_stated_rights is not None else []
        self.pf_stated_rights = [v if isinstance(v, str) else str(v) for v in self.pf_stated_rights]

        if self.pf_inquiry_contact is not None and not isinstance(self.pf_inquiry_contact, str):
            self.pf_inquiry_contact = str(self.pf_inquiry_contact)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PfControl(YAMLRoot):
    """
    A measure that treats a privacy risk by making it less likely or less harmful, the principles it serves and how
    far it has been put into effect.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO29100["PfControl"]
    class_class_curie: ClassVar[str] = "iso29100:PfControl"
    class_name: ClassVar[str] = "PfControl"
    class_model_uri: ClassVar[URIRef] = ISO29100.PfControl

    pf_id: Union[str, PfControlPfId] = None
    pf_control_kind: Union[str, "PfControlKind"] = None
    title: str = None
    pf_principles: Optional[Union[Union[str, "PfPrinciple"], list[Union[str, "PfPrinciple"]]]] = empty_list()
    pf_evidence: Optional[Union[str, list[str]]] = empty_list()
    pf_control_objective: Optional[str] = None
    pf_control_detail: Optional[str] = None
    pf_control_responsible: Optional[Union[str, PfActorPfId]] = None
    pf_control_state: Optional[Union[str, "PfImplementationState"]] = None
    pf_answers_requirements: Optional[Union[Union[str, PfSafeguardingRequirementPfId], list[Union[str, PfSafeguardingRequirementPfId]]]] = empty_list()
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.pf_id):
            self.MissingRequiredField("pf_id")
        if not isinstance(self.pf_id, PfControlPfId):
            self.pf_id = PfControlPfId(self.pf_id)

        if self._is_empty(self.pf_control_kind):
            self.MissingRequiredField("pf_control_kind")
        if not isinstance(self.pf_control_kind, PfControlKind):
            self.pf_control_kind = PfControlKind(self.pf_control_kind)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.pf_principles, list):
            self.pf_principles = [self.pf_principles] if self.pf_principles is not None else []
        self.pf_principles = [v if isinstance(v, PfPrinciple) else PfPrinciple(v) for v in self.pf_principles]

        if not isinstance(self.pf_evidence, list):
            self.pf_evidence = [self.pf_evidence] if self.pf_evidence is not None else []
        self.pf_evidence = [v if isinstance(v, str) else str(v) for v in self.pf_evidence]

        if self.pf_control_objective is not None and not isinstance(self.pf_control_objective, str):
            self.pf_control_objective = str(self.pf_control_objective)

        if self.pf_control_detail is not None and not isinstance(self.pf_control_detail, str):
            self.pf_control_detail = str(self.pf_control_detail)

        if self.pf_control_responsible is not None and not isinstance(self.pf_control_responsible, PfActorPfId):
            self.pf_control_responsible = PfActorPfId(self.pf_control_responsible)

        if self.pf_control_state is not None and not isinstance(self.pf_control_state, PfImplementationState):
            self.pf_control_state = PfImplementationState(self.pf_control_state)

        if not isinstance(self.pf_answers_requirements, list):
            self.pf_answers_requirements = [self.pf_answers_requirements] if self.pf_answers_requirements is not None else []
        self.pf_answers_requirements = [v if isinstance(v, PfSafeguardingRequirementPfId) else PfSafeguardingRequirementPfId(v) for v in self.pf_answers_requirements]

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PfPrincipleImplementation(YAMLRoot):
    """
    How the organization stands against one privacy principle: what it does, what shows it, and what is still missing.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO29100["PfPrincipleImplementation"]
    class_class_curie: ClassVar[str] = "iso29100:PfPrincipleImplementation"
    class_name: ClassVar[str] = "PfPrincipleImplementation"
    class_model_uri: ClassVar[URIRef] = ISO29100.PfPrincipleImplementation

    pf_id: Union[str, PfPrincipleImplementationPfId] = None
    pf_principle: Union[str, "PfPrinciple"] = None
    title: str = None
    pf_related_controls: Optional[Union[Union[str, PfControlPfId], list[Union[str, PfControlPfId]]]] = empty_list()
    pf_evidence: Optional[Union[str, list[str]]] = empty_list()
    pf_measures: Optional[Union[str, list[str]]] = empty_list()
    pf_gaps: Optional[Union[str, list[str]]] = empty_list()
    pf_improvements: Optional[Union[str, list[str]]] = empty_list()
    pf_last_assessed: Optional[Union[str, XSDDate]] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.pf_id):
            self.MissingRequiredField("pf_id")
        if not isinstance(self.pf_id, PfPrincipleImplementationPfId):
            self.pf_id = PfPrincipleImplementationPfId(self.pf_id)

        if self._is_empty(self.pf_principle):
            self.MissingRequiredField("pf_principle")
        if not isinstance(self.pf_principle, PfPrinciple):
            self.pf_principle = PfPrinciple(self.pf_principle)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.pf_related_controls, list):
            self.pf_related_controls = [self.pf_related_controls] if self.pf_related_controls is not None else []
        self.pf_related_controls = [v if isinstance(v, PfControlPfId) else PfControlPfId(v) for v in self.pf_related_controls]

        if not isinstance(self.pf_evidence, list):
            self.pf_evidence = [self.pf_evidence] if self.pf_evidence is not None else []
        self.pf_evidence = [v if isinstance(v, str) else str(v) for v in self.pf_evidence]

        if not isinstance(self.pf_measures, list):
            self.pf_measures = [self.pf_measures] if self.pf_measures is not None else []
        self.pf_measures = [v if isinstance(v, str) else str(v) for v in self.pf_measures]

        if not isinstance(self.pf_gaps, list):
            self.pf_gaps = [self.pf_gaps] if self.pf_gaps is not None else []
        self.pf_gaps = [v if isinstance(v, str) else str(v) for v in self.pf_gaps]

        if not isinstance(self.pf_improvements, list):
            self.pf_improvements = [self.pf_improvements] if self.pf_improvements is not None else []
        self.pf_improvements = [v if isinstance(v, str) else str(v) for v in self.pf_improvements]

        if self.pf_last_assessed is not None and not isinstance(self.pf_last_assessed, XSDDate):
            self.pf_last_assessed = XSDDate(self.pf_last_assessed)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PfRisk(YAMLRoot):
    """
    A way that handling PII could harm people: where the risk comes from, how likely and how bad it is, and what is
    done about it.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO29100["PfRisk"]
    class_class_curie: ClassVar[str] = "iso29100:PfRisk"
    class_name: ClassVar[str] = "PfRisk"
    class_model_uri: ClassVar[URIRef] = ISO29100.PfRisk

    pf_id: Union[str, PfRiskPfId] = None
    title: str = None
    pf_concerned_pii: Optional[Union[Union[str, PfPiiItemPfId], list[Union[str, PfPiiItemPfId]]]] = empty_list()
    pf_concerned_principals: Optional[Union[Union[str, PfPiiPrincipalPfId], list[Union[str, PfPiiPrincipalPfId]]]] = empty_list()
    pf_related_controls: Optional[Union[Union[str, PfControlPfId], list[Union[str, PfControlPfId]]]] = empty_list()
    pf_risk_source: Optional[str] = None
    pf_risk_likelihood: Optional[str] = None
    pf_risk_consequence: Optional[str] = None
    pf_risk_inherent_level: Optional[Union[str, "PfRiskLevel"]] = None
    pf_risk_residual_level: Optional[Union[str, "PfRiskLevel"]] = None
    pf_risk_owner: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.pf_id):
            self.MissingRequiredField("pf_id")
        if not isinstance(self.pf_id, PfRiskPfId):
            self.pf_id = PfRiskPfId(self.pf_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.pf_concerned_pii, list):
            self.pf_concerned_pii = [self.pf_concerned_pii] if self.pf_concerned_pii is not None else []
        self.pf_concerned_pii = [v if isinstance(v, PfPiiItemPfId) else PfPiiItemPfId(v) for v in self.pf_concerned_pii]

        if not isinstance(self.pf_concerned_principals, list):
            self.pf_concerned_principals = [self.pf_concerned_principals] if self.pf_concerned_principals is not None else []
        self.pf_concerned_principals = [v if isinstance(v, PfPiiPrincipalPfId) else PfPiiPrincipalPfId(v) for v in self.pf_concerned_principals]

        if not isinstance(self.pf_related_controls, list):
            self.pf_related_controls = [self.pf_related_controls] if self.pf_related_controls is not None else []
        self.pf_related_controls = [v if isinstance(v, PfControlPfId) else PfControlPfId(v) for v in self.pf_related_controls]

        if self.pf_risk_source is not None and not isinstance(self.pf_risk_source, str):
            self.pf_risk_source = str(self.pf_risk_source)

        if self.pf_risk_likelihood is not None and not isinstance(self.pf_risk_likelihood, str):
            self.pf_risk_likelihood = str(self.pf_risk_likelihood)

        if self.pf_risk_consequence is not None and not isinstance(self.pf_risk_consequence, str):
            self.pf_risk_consequence = str(self.pf_risk_consequence)

        if self.pf_risk_inherent_level is not None and not isinstance(self.pf_risk_inherent_level, PfRiskLevel):
            self.pf_risk_inherent_level = PfRiskLevel(self.pf_risk_inherent_level)

        if self.pf_risk_residual_level is not None and not isinstance(self.pf_risk_residual_level, PfRiskLevel):
            self.pf_risk_residual_level = PfRiskLevel(self.pf_risk_residual_level)

        if self.pf_risk_owner is not None and not isinstance(self.pf_risk_owner, str):
            self.pf_risk_owner = str(self.pf_risk_owner)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PfImpactAssessment(YAMLRoot):
    """
    A review of what a system or activity could do to people's privacy, the risks it found and what became of them.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO29100["PfImpactAssessment"]
    class_class_curie: ClassVar[str] = "iso29100:PfImpactAssessment"
    class_name: ClassVar[str] = "PfImpactAssessment"
    class_model_uri: ClassVar[URIRef] = ISO29100.PfImpactAssessment

    pf_id: Union[str, PfImpactAssessmentPfId] = None
    title: str = None
    pf_assessment_scope: Optional[str] = None
    pf_assessment_date: Optional[Union[str, XSDDate]] = None
    pf_assessor: Optional[str] = None
    pf_assessed_activities: Optional[Union[Union[str, PfProcessingActivityPfId], list[Union[str, PfProcessingActivityPfId]]]] = empty_list()
    pf_risks_found: Optional[Union[Union[str, PfRiskPfId], list[Union[str, PfRiskPfId]]]] = empty_list()
    pf_risks_treated: Optional[Union[Union[str, PfRiskPfId], list[Union[str, PfRiskPfId]]]] = empty_list()
    pf_risks_accepted: Optional[Union[Union[str, PfRiskPfId], list[Union[str, PfRiskPfId]]]] = empty_list()
    pf_assessment_outcome: Optional[str] = None
    pf_consultations: Optional[Union[str, list[str]]] = empty_list()
    pf_next_assessment: Optional[Union[str, XSDDate]] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.pf_id):
            self.MissingRequiredField("pf_id")
        if not isinstance(self.pf_id, PfImpactAssessmentPfId):
            self.pf_id = PfImpactAssessmentPfId(self.pf_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self.pf_assessment_scope is not None and not isinstance(self.pf_assessment_scope, str):
            self.pf_assessment_scope = str(self.pf_assessment_scope)

        if self.pf_assessment_date is not None and not isinstance(self.pf_assessment_date, XSDDate):
            self.pf_assessment_date = XSDDate(self.pf_assessment_date)

        if self.pf_assessor is not None and not isinstance(self.pf_assessor, str):
            self.pf_assessor = str(self.pf_assessor)

        if not isinstance(self.pf_assessed_activities, list):
            self.pf_assessed_activities = [self.pf_assessed_activities] if self.pf_assessed_activities is not None else []
        self.pf_assessed_activities = [v if isinstance(v, PfProcessingActivityPfId) else PfProcessingActivityPfId(v) for v in self.pf_assessed_activities]

        if not isinstance(self.pf_risks_found, list):
            self.pf_risks_found = [self.pf_risks_found] if self.pf_risks_found is not None else []
        self.pf_risks_found = [v if isinstance(v, PfRiskPfId) else PfRiskPfId(v) for v in self.pf_risks_found]

        if not isinstance(self.pf_risks_treated, list):
            self.pf_risks_treated = [self.pf_risks_treated] if self.pf_risks_treated is not None else []
        self.pf_risks_treated = [v if isinstance(v, PfRiskPfId) else PfRiskPfId(v) for v in self.pf_risks_treated]

        if not isinstance(self.pf_risks_accepted, list):
            self.pf_risks_accepted = [self.pf_risks_accepted] if self.pf_risks_accepted is not None else []
        self.pf_risks_accepted = [v if isinstance(v, PfRiskPfId) else PfRiskPfId(v) for v in self.pf_risks_accepted]

        if self.pf_assessment_outcome is not None and not isinstance(self.pf_assessment_outcome, str):
            self.pf_assessment_outcome = str(self.pf_assessment_outcome)

        if not isinstance(self.pf_consultations, list):
            self.pf_consultations = [self.pf_consultations] if self.pf_consultations is not None else []
        self.pf_consultations = [v if isinstance(v, str) else str(v) for v in self.pf_consultations]

        if self.pf_next_assessment is not None and not isinstance(self.pf_next_assessment, XSDDate):
            self.pf_next_assessment = XSDDate(self.pf_next_assessment)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PfBreach(YAMLRoot):
    """
    A time when PII was handled against a safeguarding requirement: what happened, who was told and what was done.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO29100["PfBreach"]
    class_class_curie: ClassVar[str] = "iso29100:PfBreach"
    class_name: ClassVar[str] = "PfBreach"
    class_model_uri: ClassVar[URIRef] = ISO29100.PfBreach

    pf_id: Union[str, PfBreachPfId] = None
    title: str = None
    pf_concerned_pii: Optional[Union[Union[str, PfPiiItemPfId], list[Union[str, PfPiiItemPfId]]]] = empty_list()
    pf_breach_occurred: Optional[Union[str, XSDDateTime]] = None
    pf_breach_discovered: Optional[Union[str, XSDDateTime]] = None
    pf_breach_closed: Optional[Union[str, XSDDateTime]] = None
    pf_principals_affected: Optional[int] = None
    pf_breached_requirements: Optional[Union[Union[str, PfSafeguardingRequirementPfId], list[Union[str, PfSafeguardingRequirementPfId]]]] = empty_list()
    pf_breach_severity: Optional[Union[str, "PfRiskLevel"]] = None
    pf_immediate_actions: Optional[Union[str, list[str]]] = empty_list()
    pf_notification_required: Optional[Union[bool, Bool]] = None
    pf_notifications: Optional[Union[str, list[str]]] = empty_list()
    pf_remediation: Optional[Union[str, list[str]]] = empty_list()
    pf_lessons: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.pf_id):
            self.MissingRequiredField("pf_id")
        if not isinstance(self.pf_id, PfBreachPfId):
            self.pf_id = PfBreachPfId(self.pf_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.pf_concerned_pii, list):
            self.pf_concerned_pii = [self.pf_concerned_pii] if self.pf_concerned_pii is not None else []
        self.pf_concerned_pii = [v if isinstance(v, PfPiiItemPfId) else PfPiiItemPfId(v) for v in self.pf_concerned_pii]

        if self.pf_breach_occurred is not None and not isinstance(self.pf_breach_occurred, XSDDateTime):
            self.pf_breach_occurred = XSDDateTime(self.pf_breach_occurred)

        if self.pf_breach_discovered is not None and not isinstance(self.pf_breach_discovered, XSDDateTime):
            self.pf_breach_discovered = XSDDateTime(self.pf_breach_discovered)

        if self.pf_breach_closed is not None and not isinstance(self.pf_breach_closed, XSDDateTime):
            self.pf_breach_closed = XSDDateTime(self.pf_breach_closed)

        if self.pf_principals_affected is not None and not isinstance(self.pf_principals_affected, int):
            self.pf_principals_affected = int(self.pf_principals_affected)

        if not isinstance(self.pf_breached_requirements, list):
            self.pf_breached_requirements = [self.pf_breached_requirements] if self.pf_breached_requirements is not None else []
        self.pf_breached_requirements = [v if isinstance(v, PfSafeguardingRequirementPfId) else PfSafeguardingRequirementPfId(v) for v in self.pf_breached_requirements]

        if self.pf_breach_severity is not None and not isinstance(self.pf_breach_severity, PfRiskLevel):
            self.pf_breach_severity = PfRiskLevel(self.pf_breach_severity)

        if not isinstance(self.pf_immediate_actions, list):
            self.pf_immediate_actions = [self.pf_immediate_actions] if self.pf_immediate_actions is not None else []
        self.pf_immediate_actions = [v if isinstance(v, str) else str(v) for v in self.pf_immediate_actions]

        if self.pf_notification_required is not None and not isinstance(self.pf_notification_required, Bool):
            self.pf_notification_required = Bool(self.pf_notification_required)

        if not isinstance(self.pf_notifications, list):
            self.pf_notifications = [self.pf_notifications] if self.pf_notifications is not None else []
        self.pf_notifications = [v if isinstance(v, str) else str(v) for v in self.pf_notifications]

        if not isinstance(self.pf_remediation, list):
            self.pf_remediation = [self.pf_remediation] if self.pf_remediation is not None else []
        self.pf_remediation = [v if isinstance(v, str) else str(v) for v in self.pf_remediation]

        if self.pf_lessons is not None and not isinstance(self.pf_lessons, str):
            self.pf_lessons = str(self.pf_lessons)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PfConsent(YAMLRoot):
    """
    One person's agreement to the processing of their PII for stated purposes, and where it stands.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO29100["PfConsent"]
    class_class_curie: ClassVar[str] = "iso29100:PfConsent"
    class_name: ClassVar[str] = "PfConsent"
    class_model_uri: ClassVar[URIRef] = ISO29100.PfConsent

    pf_id: Union[str, PfConsentPfId] = None
    pf_principal: Union[str, PfPiiPrincipalPfId] = None
    pf_consent_state: Union[str, "PfConsentState"] = None
    title: str = None
    pf_purposes: Optional[Union[str, list[str]]] = empty_list()
    pf_concerned_pii: Optional[Union[Union[str, PfPiiItemPfId], list[Union[str, PfPiiItemPfId]]]] = empty_list()
    pf_evidence: Optional[Union[str, list[str]]] = empty_list()
    pf_consent_mechanism: Optional[Union[str, "PfConsentMechanism"]] = None
    pf_consent_given: Optional[Union[str, XSDDateTime]] = None
    pf_consent_withdrawn: Optional[Union[str, XSDDateTime]] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.pf_id):
            self.MissingRequiredField("pf_id")
        if not isinstance(self.pf_id, PfConsentPfId):
            self.pf_id = PfConsentPfId(self.pf_id)

        if self._is_empty(self.pf_principal):
            self.MissingRequiredField("pf_principal")
        if not isinstance(self.pf_principal, PfPiiPrincipalPfId):
            self.pf_principal = PfPiiPrincipalPfId(self.pf_principal)

        if self._is_empty(self.pf_consent_state):
            self.MissingRequiredField("pf_consent_state")
        if not isinstance(self.pf_consent_state, PfConsentState):
            self.pf_consent_state = PfConsentState(self.pf_consent_state)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.pf_purposes, list):
            self.pf_purposes = [self.pf_purposes] if self.pf_purposes is not None else []
        self.pf_purposes = [v if isinstance(v, str) else str(v) for v in self.pf_purposes]

        if not isinstance(self.pf_concerned_pii, list):
            self.pf_concerned_pii = [self.pf_concerned_pii] if self.pf_concerned_pii is not None else []
        self.pf_concerned_pii = [v if isinstance(v, PfPiiItemPfId) else PfPiiItemPfId(v) for v in self.pf_concerned_pii]

        if not isinstance(self.pf_evidence, list):
            self.pf_evidence = [self.pf_evidence] if self.pf_evidence is not None else []
        self.pf_evidence = [v if isinstance(v, str) else str(v) for v in self.pf_evidence]

        if self.pf_consent_mechanism is not None and not isinstance(self.pf_consent_mechanism, PfConsentMechanism):
            self.pf_consent_mechanism = PfConsentMechanism(self.pf_consent_mechanism)

        if self.pf_consent_given is not None and not isinstance(self.pf_consent_given, XSDDateTime):
            self.pf_consent_given = XSDDateTime(self.pf_consent_given)

        if self.pf_consent_withdrawn is not None and not isinstance(self.pf_consent_withdrawn, XSDDateTime):
            self.pf_consent_withdrawn = XSDDateTime(self.pf_consent_withdrawn)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PfPreference(YAMLRoot):
    """
    What one person has said they want done, or not done, with their PII.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO29100["PfPreference"]
    class_class_curie: ClassVar[str] = "iso29100:PfPreference"
    class_name: ClassVar[str] = "PfPreference"
    class_model_uri: ClassVar[URIRef] = ISO29100.PfPreference

    pf_id: Union[str, PfPreferencePfId] = None
    pf_principal: Union[str, PfPiiPrincipalPfId] = None
    title: str = None
    pf_preference_scope: Optional[str] = None
    pf_wants_anonymity: Optional[Union[bool, Bool]] = None
    pf_wants_pseudonymity: Optional[Union[bool, Bool]] = None
    pf_refused_operations: Optional[Union[Union[str, "PfOperation"], list[Union[str, "PfOperation"]]]] = empty_list()
    pf_refused_recipients: Optional[Union[str, list[str]]] = empty_list()
    pf_preference_recorded: Optional[Union[str, XSDDate]] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.pf_id):
            self.MissingRequiredField("pf_id")
        if not isinstance(self.pf_id, PfPreferencePfId):
            self.pf_id = PfPreferencePfId(self.pf_id)

        if self._is_empty(self.pf_principal):
            self.MissingRequiredField("pf_principal")
        if not isinstance(self.pf_principal, PfPiiPrincipalPfId):
            self.pf_principal = PfPiiPrincipalPfId(self.pf_principal)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self.pf_preference_scope is not None and not isinstance(self.pf_preference_scope, str):
            self.pf_preference_scope = str(self.pf_preference_scope)

        if self.pf_wants_anonymity is not None and not isinstance(self.pf_wants_anonymity, Bool):
            self.pf_wants_anonymity = Bool(self.pf_wants_anonymity)

        if self.pf_wants_pseudonymity is not None and not isinstance(self.pf_wants_pseudonymity, Bool):
            self.pf_wants_pseudonymity = Bool(self.pf_wants_pseudonymity)

        if not isinstance(self.pf_refused_operations, list):
            self.pf_refused_operations = [self.pf_refused_operations] if self.pf_refused_operations is not None else []
        self.pf_refused_operations = [v if isinstance(v, PfOperation) else PfOperation(v) for v in self.pf_refused_operations]

        if not isinstance(self.pf_refused_recipients, list):
            self.pf_refused_recipients = [self.pf_refused_recipients] if self.pf_refused_recipients is not None else []
        self.pf_refused_recipients = [v if isinstance(v, str) else str(v) for v in self.pf_refused_recipients]

        if self.pf_preference_recorded is not None and not isinstance(self.pf_preference_recorded, XSDDate):
            self.pf_preference_recorded = XSDDate(self.pf_preference_recorded)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


# Enumerations
class PfPrinciple(EnumDefinitionImpl):
    """
    The privacy principles by their subclause numbers. A value's title and description are this project's own summary,
    and the principles' headings and wording are ISO's.
    """
    principle_6_2 = PermissibleValue(
        text="principle_6_2",
        title="6.2 People decide",
        description="""People get a say in whether their PII is processed, can agree or refuse purpose by purpose, and can change their minds later.""")
    principle_6_3 = PermissibleValue(
        text="principle_6_3",
        title="6.3 Lawful, stated reasons",
        description="""The law allows each reason for processing, and people are told the reason before their PII is gathered, or at that moment.""")
    principle_6_4 = PermissibleValue(
        text="principle_6_4",
        title="6.4 Gather within bounds",
        description="The organization gathers only the PII that the law allows and its stated reasons need.")
    principle_6_5 = PermissibleValue(
        text="principle_6_5",
        title="6.5 A small footprint",
        description="""Systems and procedures are built to touch as little PII as they can, and as few people as possible can reach it.""")
    principle_6_6 = PermissibleValue(
        text="principle_6_6",
        title="6.6 Bounded use and keeping",
        description="""PII is used, shared and kept only as far as the stated reasons go, and is safely disposed of afterwards.""")
    principle_6_7 = PermissibleValue(
        text="principle_6_7",
        title="6.7 Correct and fit",
        description="""PII stays right, whole, up to date and suited to its use, and there are ways to check and fix it.""")
    principle_6_8 = PermissibleValue(
        text="principle_6_8",
        title="6.8 Say what happens",
        description="""People can easily find out what the organization does with PII, and hear about important changes.""")
    principle_6_9 = PermissibleValue(
        text="principle_6_9",
        title="6.9 People see their own",
        description="People can look at the PII held about them and dispute it, within what the law allows.")
    principle_6_10 = PermissibleValue(
        text="principle_6_10",
        title="6.10 Answer for it",
        description="""The organization writes down its duties, keeps protection in place when PII passes to others, and handles complaints and redress.""")
    principle_6_11 = PermissibleValue(
        text="principle_6_11",
        title="6.11 Keep it safe",
        description="""Security measures at every level guard PII against loss and unauthorized reach for as long as it is held.""")
    principle_6_12 = PermissibleValue(
        text="principle_6_12",
        title="6.12 Show the rules are met",
        description="""The organization checks, and can prove, that it meets its privacy duties, through audits and regular risk assessment.""")

    _defn = EnumDefinition(
        name="PfPrinciple",
        description="""The privacy principles by their subclause numbers. A value's title and description are this project's own summary, and the principles' headings and wording are ISO's.""",
    )

class PfOperation(EnumDefinitionImpl):
    """
    The things an organization can do to PII.
    """
    collect = PermissibleValue(
        text="collect",
        description="Get PII from the person it is about, or from another source.")
    store = PermissibleValue(
        text="store",
        description="Hold PII on a lasting medium.")
    retrieve = PermissibleValue(
        text="retrieve",
        description="Fetch stored PII for use.")
    consult = PermissibleValue(
        text="consult",
        description="Look at PII without taking a copy away.")
    alter = PermissibleValue(
        text="alter",
        description="Change PII that is already held.")
    pseudonymize = PermissibleValue(
        text="pseudonymize",
        description="Swap identifying details for an alias, in a way someone can still trace back.")
    anonymize = PermissibleValue(
        text="anonymize",
        description="Change PII so that nobody can trace it back to a person again.")
    disclose = PermissibleValue(
        text="disclose",
        description="Make PII available to another party.")
    disseminate = PermissibleValue(
        text="disseminate",
        description="Spread PII widely, such as by publishing it.")
    delete = PermissibleValue(
        text="delete",
        description="Remove PII so that it can no longer be reached or used.")
    destroy = PermissibleValue(
        text="destroy",
        description="Remove PII and whatever carried it, beyond recovery.")

    _defn = EnumDefinition(
        name="PfOperation",
        description="The things an organization can do to PII.",
    )

class PfPiiRecognition(EnumDefinitionImpl):
    """
    The ways information turns out to be PII, which a record lists so that a reader can see why the item counts.
    """
    direct_identifier = PermissibleValue(
        text="direct_identifier",
        description="It singles out one person by itself, such as a passport number.")
    distinguishing_trait = PermissibleValue(
        text="distinguishing_trait",
        description="""It sets one person apart, alone or with other details, such as a rare job title in a small town.""")
    linked_information = PermissibleValue(
        text="linked_information",
        description="It says something about a person who is already known, or can be joined to a record that does.")
    pseudonym = PermissibleValue(
        text="pseudonym",
        description="It holds an alias in place of an identifier, and the alias can be traced.")
    metadata = PermissibleValue(
        text="metadata",
        description="It describes other data, such as a message's sender and time, and so reveals a person.")
    unsolicited = PermissibleValue(
        text="unsolicited",
        description="The organization received it without asking for it.")

    _defn = EnumDefinition(
        name="PfPiiRecognition",
        description="""The ways information turns out to be PII, which a record lists so that a reader can see why the item counts.""",
    )

class PfSensitivity(EnumDefinitionImpl):
    """
    How much harm the PII could do to the person it is about.
    """
    ordinary = PermissibleValue(
        text="ordinary",
        description="It needs the usual protection for PII.")
    sensitive = PermissibleValue(
        text="sensitive",
        description="""Its misuse could badly harm the person, or a law sets it apart, such as health data, so it needs stronger protection.""")

    _defn = EnumDefinition(
        name="PfSensitivity",
        description="How much harm the PII could do to the person it is about.",
    )

class PfRequirementFactor(EnumDefinitionImpl):
    """
    Where a requirement to safeguard PII comes from.
    """
    law = PermissibleValue(
        text="law",
        description="A statute, a regulation, a court's ruling or a collective agreement.")
    contract = PermissibleValue(
        text="contract",
        description="""An agreement between parties, such as one with a processor, or rules that bind a group of companies.""")
    business = PermissibleValue(
        text="business",
        description="How the business or its application works, or a code of practice it chose to follow.")
    other = PermissibleValue(
        text="other",
        description="""Another source, such as what people have said they prefer, or a technical standard the organization adopted.""")

    _defn = EnumDefinition(
        name="PfRequirementFactor",
        description="Where a requirement to safeguard PII comes from.",
    )

class PfPolicyAudience(EnumDefinitionImpl):
    """
    Who a privacy policy is written for.
    """
    internal = PermissibleValue(
        text="internal",
        description="People inside the organization, who act on its commitments.")
    public_notice = PermissibleValue(
        text="public_notice",
        description="The people whose PII it handles, who read it to learn what happens.")

    _defn = EnumDefinition(
        name="PfPolicyAudience",
        description="Who a privacy policy is written for.",
    )

class PfControlKind(EnumDefinitionImpl):
    """
    The form a control takes.
    """
    organizational = PermissibleValue(
        text="organizational",
        description="A policy, a procedure, a role or another way of running things.")
    physical = PermissibleValue(
        text="physical",
        description="A measure that guards the places and equipment where PII sits.")
    technical = PermissibleValue(
        text="technical",
        description="A system, product or service that protects PII.")
    privacy_enhancing_technology = PermissibleValue(
        text="privacy_enhancing_technology",
        description="A technical measure built to reduce what is collected or revealed about people.")
    contractual = PermissibleValue(
        text="contractual",
        description="A binding agreement, such as one with a processor or across a group of companies.")

    _defn = EnumDefinition(
        name="PfControlKind",
        description="The form a control takes.",
    )

class PfImplementationState(EnumDefinitionImpl):
    """
    How far a control has been put into effect.
    """
    planned = PermissibleValue(
        text="planned",
        description="It is decided on but not started.")
    in_progress = PermissibleValue(
        text="in_progress",
        description="It is being put in place.")
    in_operation = PermissibleValue(
        text="in_operation",
        description="It is in place and working.")
    retired = PermissibleValue(
        text="retired",
        description="It is no longer in use.")

    _defn = EnumDefinition(
        name="PfImplementationState",
        description="How far a control has been put into effect.",
    )

class PfRiskLevel(EnumDefinitionImpl):
    """
    A qualitative level of risk to people, offered for an organization that adopts it, since the framework leaves the
    scale to the organization.
    """
    low = PermissibleValue(
        text="low",
        description="The harm to people would be limited.")
    medium = PermissibleValue(
        text="medium",
        description="The harm would call for planned measures.")
    high = PermissibleValue(
        text="high",
        description="The harm could be serious.")
    very_high = PermissibleValue(
        text="very_high",
        description="The harm could be severe or lasting, and needs treating at once.")

    _defn = EnumDefinition(
        name="PfRiskLevel",
        description="""A qualitative level of risk to people, offered for an organization that adopts it, since the framework leaves the scale to the organization.""",
    )

class PfConsentMechanism(EnumDefinitionImpl):
    """
    How a person's agreement to processing is obtained.
    """
    opt_in = PermissibleValue(
        text="opt_in",
        description="The person acts to agree before the processing starts.")
    opt_out = PermissibleValue(
        text="opt_out",
        description="The processing goes ahead unless the person acts to refuse it.")
    implied = PermissibleValue(
        text="implied",
        description="""Something the person does shows agreement, such as placing an order, where the law allows that reading.""")

    _defn = EnumDefinition(
        name="PfConsentMechanism",
        description="How a person's agreement to processing is obtained.",
    )

class PfConsentState(EnumDefinitionImpl):
    """
    Where a person's agreement stands.
    """
    given = PermissibleValue(
        text="given",
        description="The agreement holds.")
    refused = PermissibleValue(
        text="refused",
        description="The person said no.")
    withdrawn = PermissibleValue(
        text="withdrawn",
        description="The person took back an agreement they had given.")
    expired = PermissibleValue(
        text="expired",
        description="The agreement ran out.")

    _defn = EnumDefinition(
        name="PfConsentState",
        description="Where a person's agreement stands.",
    )

# Slots
class slots:
    pass

slots.pf_id = Slot(uri=ISO29100.pf_id, name="pf_id", curie=ISO29100.curie('pf_id'),
                   model_uri=ISO29100.pf_id, domain=None, range=URIRef)

slots.title = Slot(uri=SCHEMA.name, name="title", curie=SCHEMA.curie('name'),
                   model_uri=ISO29100.title, domain=None, range=Optional[str])

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=ISO29100.description, domain=None, range=Optional[str])

slots.pf_actor_type = Slot(uri=ISO29100.pf_actor_type, name="pf_actor_type", curie=ISO29100.curie('pf_actor_type'),
                   model_uri=ISO29100.pf_actor_type, domain=None, range=Optional[str])

slots.pf_jurisdictions = Slot(uri=ISO29100.pf_jurisdictions, name="pf_jurisdictions", curie=ISO29100.curie('pf_jurisdictions'),
                   model_uri=ISO29100.pf_jurisdictions, domain=None, range=Optional[Union[str, list[str]]])

slots.pf_purposes = Slot(uri=ISO29100.pf_purposes, name="pf_purposes", curie=ISO29100.curie('pf_purposes'),
                   model_uri=ISO29100.pf_purposes, domain=None, range=Optional[Union[str, list[str]]])

slots.pf_legal_bases = Slot(uri=ISO29100.pf_legal_bases, name="pf_legal_bases", curie=ISO29100.curie('pf_legal_bases'),
                   model_uri=ISO29100.pf_legal_bases, domain=None, range=Optional[Union[str, list[str]]])

slots.pf_operations = Slot(uri=ISO29100.pf_operations, name="pf_operations", curie=ISO29100.curie('pf_operations'),
                   model_uri=ISO29100.pf_operations, domain=None, range=Optional[Union[Union[str, "PfOperation"], list[Union[str, "PfOperation"]]]])

slots.pf_retention = Slot(uri=ISO29100.pf_retention, name="pf_retention", curie=ISO29100.curie('pf_retention'),
                   model_uri=ISO29100.pf_retention, domain=None, range=Optional[Union[str, PfDuration]])

slots.pf_principles = Slot(uri=ISO29100.pf_principles, name="pf_principles", curie=ISO29100.curie('pf_principles'),
                   model_uri=ISO29100.pf_principles, domain=None, range=Optional[Union[Union[str, "PfPrinciple"], list[Union[str, "PfPrinciple"]]]])

slots.pf_concerned_pii = Slot(uri=ISO29100.pf_concerned_pii, name="pf_concerned_pii", curie=ISO29100.curie('pf_concerned_pii'),
                   model_uri=ISO29100.pf_concerned_pii, domain=None, range=Optional[Union[Union[str, PfPiiItemPfId], list[Union[str, PfPiiItemPfId]]]])

slots.pf_concerned_principals = Slot(uri=ISO29100.pf_concerned_principals, name="pf_concerned_principals", curie=ISO29100.curie('pf_concerned_principals'),
                   model_uri=ISO29100.pf_concerned_principals, domain=None, range=Optional[Union[Union[str, PfPiiPrincipalPfId], list[Union[str, PfPiiPrincipalPfId]]]])

slots.pf_principal = Slot(uri=ISO29100.pf_principal, name="pf_principal", curie=ISO29100.curie('pf_principal'),
                   model_uri=ISO29100.pf_principal, domain=None, range=Optional[Union[str, PfPiiPrincipalPfId]])

slots.pf_related_controls = Slot(uri=ISO29100.pf_related_controls, name="pf_related_controls", curie=ISO29100.curie('pf_related_controls'),
                   model_uri=ISO29100.pf_related_controls, domain=None, range=Optional[Union[Union[str, PfControlPfId], list[Union[str, PfControlPfId]]]])

slots.pf_evidence = Slot(uri=ISO29100.pf_evidence, name="pf_evidence", curie=ISO29100.curie('pf_evidence'),
                   model_uri=ISO29100.pf_evidence, domain=None, range=Optional[Union[str, list[str]]])

slots.pfFramework__pf_organization = Slot(uri=ISO29100.pf_organization, name="pfFramework__pf_organization", curie=ISO29100.curie('pf_organization'),
                   model_uri=ISO29100.pfFramework__pf_organization, domain=None, range=str)

slots.pfFramework__pf_ict_systems = Slot(uri=ISO29100.pf_ict_systems, name="pfFramework__pf_ict_systems", curie=ISO29100.curie('pf_ict_systems'),
                   model_uri=ISO29100.pfFramework__pf_ict_systems, domain=None, range=Optional[Union[str, list[str]]])

slots.pfFramework__pf_actors = Slot(uri=ISO29100.pf_actors, name="pfFramework__pf_actors", curie=ISO29100.curie('pf_actors'),
                   model_uri=ISO29100.pfFramework__pf_actors, domain=None, range=Optional[Union[dict[Union[str, PfActorPfId], Union[dict, PfActor]], list[Union[dict, PfActor]]]])

slots.pfFramework__pf_pii_items = Slot(uri=ISO29100.pf_pii_items, name="pfFramework__pf_pii_items", curie=ISO29100.curie('pf_pii_items'),
                   model_uri=ISO29100.pfFramework__pf_pii_items, domain=None, range=Optional[Union[dict[Union[str, PfPiiItemPfId], Union[dict, PfPiiItem]], list[Union[dict, PfPiiItem]]]])

slots.pfFramework__pf_flows = Slot(uri=ISO29100.pf_flows, name="pfFramework__pf_flows", curie=ISO29100.curie('pf_flows'),
                   model_uri=ISO29100.pfFramework__pf_flows, domain=None, range=Optional[Union[dict[Union[str, PfPiiFlowPfId], Union[dict, PfPiiFlow]], list[Union[dict, PfPiiFlow]]]])

slots.pfFramework__pf_processing_activities = Slot(uri=ISO29100.pf_processing_activities, name="pfFramework__pf_processing_activities", curie=ISO29100.curie('pf_processing_activities'),
                   model_uri=ISO29100.pfFramework__pf_processing_activities, domain=None, range=Optional[Union[dict[Union[str, PfProcessingActivityPfId], Union[dict, PfProcessingActivity]], list[Union[dict, PfProcessingActivity]]]])

slots.pfFramework__pf_safeguarding_requirements = Slot(uri=ISO29100.pf_safeguarding_requirements, name="pfFramework__pf_safeguarding_requirements", curie=ISO29100.curie('pf_safeguarding_requirements'),
                   model_uri=ISO29100.pfFramework__pf_safeguarding_requirements, domain=None, range=Optional[Union[dict[Union[str, PfSafeguardingRequirementPfId], Union[dict, PfSafeguardingRequirement]], list[Union[dict, PfSafeguardingRequirement]]]])

slots.pfFramework__pf_policies = Slot(uri=ISO29100.pf_policies, name="pfFramework__pf_policies", curie=ISO29100.curie('pf_policies'),
                   model_uri=ISO29100.pfFramework__pf_policies, domain=None, range=Optional[Union[dict[Union[str, PfPolicyPfId], Union[dict, PfPolicy]], list[Union[dict, PfPolicy]]]])

slots.pfFramework__pf_controls = Slot(uri=ISO29100.pf_controls, name="pfFramework__pf_controls", curie=ISO29100.curie('pf_controls'),
                   model_uri=ISO29100.pfFramework__pf_controls, domain=None, range=Optional[Union[dict[Union[str, PfControlPfId], Union[dict, PfControl]], list[Union[dict, PfControl]]]])

slots.pfFramework__pf_principle_implementations = Slot(uri=ISO29100.pf_principle_implementations, name="pfFramework__pf_principle_implementations", curie=ISO29100.curie('pf_principle_implementations'),
                   model_uri=ISO29100.pfFramework__pf_principle_implementations, domain=None, range=Optional[Union[dict[Union[str, PfPrincipleImplementationPfId], Union[dict, PfPrincipleImplementation]], list[Union[dict, PfPrincipleImplementation]]]])

slots.pfFramework__pf_risks = Slot(uri=ISO29100.pf_risks, name="pfFramework__pf_risks", curie=ISO29100.curie('pf_risks'),
                   model_uri=ISO29100.pfFramework__pf_risks, domain=None, range=Optional[Union[dict[Union[str, PfRiskPfId], Union[dict, PfRisk]], list[Union[dict, PfRisk]]]])

slots.pfFramework__pf_impact_assessments = Slot(uri=ISO29100.pf_impact_assessments, name="pfFramework__pf_impact_assessments", curie=ISO29100.curie('pf_impact_assessments'),
                   model_uri=ISO29100.pfFramework__pf_impact_assessments, domain=None, range=Optional[Union[dict[Union[str, PfImpactAssessmentPfId], Union[dict, PfImpactAssessment]], list[Union[dict, PfImpactAssessment]]]])

slots.pfFramework__pf_breaches = Slot(uri=ISO29100.pf_breaches, name="pfFramework__pf_breaches", curie=ISO29100.curie('pf_breaches'),
                   model_uri=ISO29100.pfFramework__pf_breaches, domain=None, range=Optional[Union[dict[Union[str, PfBreachPfId], Union[dict, PfBreach]], list[Union[dict, PfBreach]]]])

slots.pfFramework__pf_consents = Slot(uri=ISO29100.pf_consents, name="pfFramework__pf_consents", curie=ISO29100.curie('pf_consents'),
                   model_uri=ISO29100.pfFramework__pf_consents, domain=None, range=Optional[Union[dict[Union[str, PfConsentPfId], Union[dict, PfConsent]], list[Union[dict, PfConsent]]]])

slots.pfFramework__pf_preferences = Slot(uri=ISO29100.pf_preferences, name="pfFramework__pf_preferences", curie=ISO29100.curie('pf_preferences'),
                   model_uri=ISO29100.pfFramework__pf_preferences, domain=None, range=Optional[Union[dict[Union[str, PfPreferencePfId], Union[dict, PfPreference]], list[Union[dict, PfPreference]]]])

slots.pfActor__pf_contact = Slot(uri=ISO29100.pf_contact, name="pfActor__pf_contact", curie=ISO29100.curie('pf_contact'),
                   model_uri=ISO29100.pfActor__pf_contact, domain=None, range=Optional[str])

slots.pfPiiController__pf_appointed_processors = Slot(uri=ISO29100.pf_appointed_processors, name="pfPiiController__pf_appointed_processors", curie=ISO29100.curie('pf_appointed_processors'),
                   model_uri=ISO29100.pfPiiController__pf_appointed_processors, domain=None, range=Optional[Union[Union[str, PfPiiProcessorPfId], list[Union[str, PfPiiProcessorPfId]]]])

slots.pfPiiController__pf_controller_policy = Slot(uri=ISO29100.pf_controller_policy, name="pfPiiController__pf_controller_policy", curie=ISO29100.curie('pf_controller_policy'),
                   model_uri=ISO29100.pfPiiController__pf_controller_policy, domain=None, range=Optional[Union[str, PfPolicyPfId]])

slots.pfPiiController__pf_privacy_officer = Slot(uri=ISO29100.pf_privacy_officer, name="pfPiiController__pf_privacy_officer", curie=ISO29100.curie('pf_privacy_officer'),
                   model_uri=ISO29100.pfPiiController__pf_privacy_officer, domain=None, range=Optional[str])

slots.pfPiiProcessor__pf_instructing_controllers = Slot(uri=ISO29100.pf_instructing_controllers, name="pfPiiProcessor__pf_instructing_controllers", curie=ISO29100.curie('pf_instructing_controllers'),
                   model_uri=ISO29100.pfPiiProcessor__pf_instructing_controllers, domain=None, range=Optional[Union[Union[str, PfPiiControllerPfId], list[Union[str, PfPiiControllerPfId]]]])

slots.pfPiiProcessor__pf_processing_agreement = Slot(uri=ISO29100.pf_processing_agreement, name="pfPiiProcessor__pf_processing_agreement", curie=ISO29100.curie('pf_processing_agreement'),
                   model_uri=ISO29100.pfPiiProcessor__pf_processing_agreement, domain=None, range=Optional[str])

slots.pfPiiProcessor__pf_sub_processors = Slot(uri=ISO29100.pf_sub_processors, name="pfPiiProcessor__pf_sub_processors", curie=ISO29100.curie('pf_sub_processors'),
                   model_uri=ISO29100.pfPiiProcessor__pf_sub_processors, domain=None, range=Optional[Union[Union[str, PfPiiProcessorPfId], list[Union[str, PfPiiProcessorPfId]]]])

slots.pfThirdParty__pf_receiving_purpose = Slot(uri=ISO29100.pf_receiving_purpose, name="pfThirdParty__pf_receiving_purpose", curie=ISO29100.curie('pf_receiving_purpose'),
                   model_uri=ISO29100.pfThirdParty__pf_receiving_purpose, domain=None, range=Optional[str])

slots.pfThirdParty__pf_transfer_basis = Slot(uri=ISO29100.pf_transfer_basis, name="pfThirdParty__pf_transfer_basis", curie=ISO29100.curie('pf_transfer_basis'),
                   model_uri=ISO29100.pfThirdParty__pf_transfer_basis, domain=None, range=Optional[str])

slots.pfPiiItem__pf_pii_categories = Slot(uri=ISO29100.pf_pii_categories, name="pfPiiItem__pf_pii_categories", curie=ISO29100.curie('pf_pii_categories'),
                   model_uri=ISO29100.pfPiiItem__pf_pii_categories, domain=None, range=Optional[Union[str, list[str]]])

slots.pfPiiItem__pf_recognized_by = Slot(uri=ISO29100.pf_recognized_by, name="pfPiiItem__pf_recognized_by", curie=ISO29100.curie('pf_recognized_by'),
                   model_uri=ISO29100.pfPiiItem__pf_recognized_by, domain=None, range=Optional[Union[Union[str, "PfPiiRecognition"], list[Union[str, "PfPiiRecognition"]]]])

slots.pfPiiItem__pf_sensitivity = Slot(uri=ISO29100.pf_sensitivity, name="pfPiiItem__pf_sensitivity", curie=ISO29100.curie('pf_sensitivity'),
                   model_uri=ISO29100.pfPiiItem__pf_sensitivity, domain=None, range=Optional[Union[str, "PfSensitivity"]])

slots.pfPiiItem__pf_pseudonymized = Slot(uri=ISO29100.pf_pseudonymized, name="pfPiiItem__pf_pseudonymized", curie=ISO29100.curie('pf_pseudonymized'),
                   model_uri=ISO29100.pfPiiItem__pf_pseudonymized, domain=None, range=Optional[Union[bool, Bool]])

slots.pfPiiItem__pf_linkability = Slot(uri=ISO29100.pf_linkability, name="pfPiiItem__pf_linkability", curie=ISO29100.curie('pf_linkability'),
                   model_uri=ISO29100.pfPiiItem__pf_linkability, domain=None, range=Optional[str])

slots.pfPiiFlow__pf_provider = Slot(uri=ISO29100.pf_provider, name="pfPiiFlow__pf_provider", curie=ISO29100.curie('pf_provider'),
                   model_uri=ISO29100.pfPiiFlow__pf_provider, domain=None, range=Union[str, PfActorPfId])

slots.pfPiiFlow__pf_recipient = Slot(uri=ISO29100.pf_recipient, name="pfPiiFlow__pf_recipient", curie=ISO29100.curie('pf_recipient'),
                   model_uri=ISO29100.pfPiiFlow__pf_recipient, domain=None, range=Union[str, PfActorPfId])

slots.pfPiiFlow__pf_decides_afterwards = Slot(uri=ISO29100.pf_decides_afterwards, name="pfPiiFlow__pf_decides_afterwards", curie=ISO29100.curie('pf_decides_afterwards'),
                   model_uri=ISO29100.pfPiiFlow__pf_decides_afterwards, domain=None, range=Optional[Union[str, PfActorPfId]])

slots.pfProcessingActivity__pf_controller = Slot(uri=ISO29100.pf_controller, name="pfProcessingActivity__pf_controller", curie=ISO29100.curie('pf_controller'),
                   model_uri=ISO29100.pfProcessingActivity__pf_controller, domain=None, range=Union[str, PfPiiControllerPfId])

slots.pfProcessingActivity__pf_processors = Slot(uri=ISO29100.pf_processors, name="pfProcessingActivity__pf_processors", curie=ISO29100.curie('pf_processors'),
                   model_uri=ISO29100.pfProcessingActivity__pf_processors, domain=None, range=Optional[Union[Union[str, PfPiiProcessorPfId], list[Union[str, PfPiiProcessorPfId]]]])

slots.pfProcessingActivity__pf_activity_flows = Slot(uri=ISO29100.pf_activity_flows, name="pfProcessingActivity__pf_activity_flows", curie=ISO29100.curie('pf_activity_flows'),
                   model_uri=ISO29100.pfProcessingActivity__pf_activity_flows, domain=None, range=Optional[Union[Union[str, PfPiiFlowPfId], list[Union[str, PfPiiFlowPfId]]]])

slots.pfProcessingActivity__pf_sensitivities = Slot(uri=ISO29100.pf_sensitivities, name="pfProcessingActivity__pf_sensitivities", curie=ISO29100.curie('pf_sensitivities'),
                   model_uri=ISO29100.pfProcessingActivity__pf_sensitivities, domain=None, range=Optional[Union[Union[str, "PfSensitivity"], list[Union[str, "PfSensitivity"]]]])

slots.pfProcessingActivity__pf_crosses_borders = Slot(uri=ISO29100.pf_crosses_borders, name="pfProcessingActivity__pf_crosses_borders", curie=ISO29100.curie('pf_crosses_borders'),
                   model_uri=ISO29100.pfProcessingActivity__pf_crosses_borders, domain=None, range=Optional[Union[bool, Bool]])

slots.pfProcessingActivity__pf_transfer_safeguards = Slot(uri=ISO29100.pf_transfer_safeguards, name="pfProcessingActivity__pf_transfer_safeguards", curie=ISO29100.curie('pf_transfer_safeguards'),
                   model_uri=ISO29100.pfProcessingActivity__pf_transfer_safeguards, domain=None, range=Optional[Union[str, list[str]]])

slots.pfSafeguardingRequirement__pf_requirement_factor = Slot(uri=ISO29100.pf_requirement_factor, name="pfSafeguardingRequirement__pf_requirement_factor", curie=ISO29100.curie('pf_requirement_factor'),
                   model_uri=ISO29100.pfSafeguardingRequirement__pf_requirement_factor, domain=None, range=Union[str, "PfRequirementFactor"])

slots.pfSafeguardingRequirement__pf_requirement_source = Slot(uri=ISO29100.pf_requirement_source, name="pfSafeguardingRequirement__pf_requirement_source", curie=ISO29100.curie('pf_requirement_source'),
                   model_uri=ISO29100.pfSafeguardingRequirement__pf_requirement_source, domain=None, range=Optional[str])

slots.pfSafeguardingRequirement__pf_applies_to = Slot(uri=ISO29100.pf_applies_to, name="pfSafeguardingRequirement__pf_applies_to", curie=ISO29100.curie('pf_applies_to'),
                   model_uri=ISO29100.pfSafeguardingRequirement__pf_applies_to, domain=None, range=Optional[Union[Union[str, PfActorPfId], list[Union[str, PfActorPfId]]]])

slots.pfSafeguardingRequirement__pf_met_by = Slot(uri=ISO29100.pf_met_by, name="pfSafeguardingRequirement__pf_met_by", curie=ISO29100.curie('pf_met_by'),
                   model_uri=ISO29100.pfSafeguardingRequirement__pf_met_by, domain=None, range=Optional[Union[Union[str, PfControlPfId], list[Union[str, PfControlPfId]]]])

slots.pfPolicy__pf_policy_audience = Slot(uri=ISO29100.pf_policy_audience, name="pfPolicy__pf_policy_audience", curie=ISO29100.curie('pf_policy_audience'),
                   model_uri=ISO29100.pfPolicy__pf_policy_audience, domain=None, range=Union[str, "PfPolicyAudience"])

slots.pfPolicy__pf_policy_version = Slot(uri=ISO29100.pf_policy_version, name="pfPolicy__pf_policy_version", curie=ISO29100.curie('pf_policy_version'),
                   model_uri=ISO29100.pfPolicy__pf_policy_version, domain=None, range=Optional[str])

slots.pfPolicy__pf_policy_scope = Slot(uri=ISO29100.pf_policy_scope, name="pfPolicy__pf_policy_scope", curie=ISO29100.curie('pf_policy_scope'),
                   model_uri=ISO29100.pfPolicy__pf_policy_scope, domain=None, range=Optional[str])

slots.pfPolicy__pf_policy_effective_date = Slot(uri=ISO29100.pf_policy_effective_date, name="pfPolicy__pf_policy_effective_date", curie=ISO29100.curie('pf_policy_effective_date'),
                   model_uri=ISO29100.pfPolicy__pf_policy_effective_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.pfPolicy__pf_policy_last_reviewed = Slot(uri=ISO29100.pf_policy_last_reviewed, name="pfPolicy__pf_policy_last_reviewed", curie=ISO29100.curie('pf_policy_last_reviewed'),
                   model_uri=ISO29100.pfPolicy__pf_policy_last_reviewed, domain=None, range=Optional[Union[str, XSDDate]])

slots.pfPolicy__pf_retention_statement = Slot(uri=ISO29100.pf_retention_statement, name="pfPolicy__pf_retention_statement", curie=ISO29100.curie('pf_retention_statement'),
                   model_uri=ISO29100.pfPolicy__pf_retention_statement, domain=None, range=Optional[str])

slots.pfPolicy__pf_stated_rights = Slot(uri=ISO29100.pf_stated_rights, name="pfPolicy__pf_stated_rights", curie=ISO29100.curie('pf_stated_rights'),
                   model_uri=ISO29100.pfPolicy__pf_stated_rights, domain=None, range=Optional[Union[str, list[str]]])

slots.pfPolicy__pf_inquiry_contact = Slot(uri=ISO29100.pf_inquiry_contact, name="pfPolicy__pf_inquiry_contact", curie=ISO29100.curie('pf_inquiry_contact'),
                   model_uri=ISO29100.pfPolicy__pf_inquiry_contact, domain=None, range=Optional[str])

slots.pfControl__pf_control_kind = Slot(uri=ISO29100.pf_control_kind, name="pfControl__pf_control_kind", curie=ISO29100.curie('pf_control_kind'),
                   model_uri=ISO29100.pfControl__pf_control_kind, domain=None, range=Union[str, "PfControlKind"])

slots.pfControl__pf_control_objective = Slot(uri=ISO29100.pf_control_objective, name="pfControl__pf_control_objective", curie=ISO29100.curie('pf_control_objective'),
                   model_uri=ISO29100.pfControl__pf_control_objective, domain=None, range=Optional[str])

slots.pfControl__pf_control_detail = Slot(uri=ISO29100.pf_control_detail, name="pfControl__pf_control_detail", curie=ISO29100.curie('pf_control_detail'),
                   model_uri=ISO29100.pfControl__pf_control_detail, domain=None, range=Optional[str])

slots.pfControl__pf_control_responsible = Slot(uri=ISO29100.pf_control_responsible, name="pfControl__pf_control_responsible", curie=ISO29100.curie('pf_control_responsible'),
                   model_uri=ISO29100.pfControl__pf_control_responsible, domain=None, range=Optional[Union[str, PfActorPfId]])

slots.pfControl__pf_control_state = Slot(uri=ISO29100.pf_control_state, name="pfControl__pf_control_state", curie=ISO29100.curie('pf_control_state'),
                   model_uri=ISO29100.pfControl__pf_control_state, domain=None, range=Optional[Union[str, "PfImplementationState"]])

slots.pfControl__pf_answers_requirements = Slot(uri=ISO29100.pf_answers_requirements, name="pfControl__pf_answers_requirements", curie=ISO29100.curie('pf_answers_requirements'),
                   model_uri=ISO29100.pfControl__pf_answers_requirements, domain=None, range=Optional[Union[Union[str, PfSafeguardingRequirementPfId], list[Union[str, PfSafeguardingRequirementPfId]]]])

slots.pfPrincipleImplementation__pf_principle = Slot(uri=ISO29100.pf_principle, name="pfPrincipleImplementation__pf_principle", curie=ISO29100.curie('pf_principle'),
                   model_uri=ISO29100.pfPrincipleImplementation__pf_principle, domain=None, range=Union[str, "PfPrinciple"])

slots.pfPrincipleImplementation__pf_measures = Slot(uri=ISO29100.pf_measures, name="pfPrincipleImplementation__pf_measures", curie=ISO29100.curie('pf_measures'),
                   model_uri=ISO29100.pfPrincipleImplementation__pf_measures, domain=None, range=Optional[Union[str, list[str]]])

slots.pfPrincipleImplementation__pf_gaps = Slot(uri=ISO29100.pf_gaps, name="pfPrincipleImplementation__pf_gaps", curie=ISO29100.curie('pf_gaps'),
                   model_uri=ISO29100.pfPrincipleImplementation__pf_gaps, domain=None, range=Optional[Union[str, list[str]]])

slots.pfPrincipleImplementation__pf_improvements = Slot(uri=ISO29100.pf_improvements, name="pfPrincipleImplementation__pf_improvements", curie=ISO29100.curie('pf_improvements'),
                   model_uri=ISO29100.pfPrincipleImplementation__pf_improvements, domain=None, range=Optional[Union[str, list[str]]])

slots.pfPrincipleImplementation__pf_last_assessed = Slot(uri=ISO29100.pf_last_assessed, name="pfPrincipleImplementation__pf_last_assessed", curie=ISO29100.curie('pf_last_assessed'),
                   model_uri=ISO29100.pfPrincipleImplementation__pf_last_assessed, domain=None, range=Optional[Union[str, XSDDate]])

slots.pfRisk__pf_risk_source = Slot(uri=ISO29100.pf_risk_source, name="pfRisk__pf_risk_source", curie=ISO29100.curie('pf_risk_source'),
                   model_uri=ISO29100.pfRisk__pf_risk_source, domain=None, range=Optional[str])

slots.pfRisk__pf_risk_likelihood = Slot(uri=ISO29100.pf_risk_likelihood, name="pfRisk__pf_risk_likelihood", curie=ISO29100.curie('pf_risk_likelihood'),
                   model_uri=ISO29100.pfRisk__pf_risk_likelihood, domain=None, range=Optional[str])

slots.pfRisk__pf_risk_consequence = Slot(uri=ISO29100.pf_risk_consequence, name="pfRisk__pf_risk_consequence", curie=ISO29100.curie('pf_risk_consequence'),
                   model_uri=ISO29100.pfRisk__pf_risk_consequence, domain=None, range=Optional[str])

slots.pfRisk__pf_risk_inherent_level = Slot(uri=ISO29100.pf_risk_inherent_level, name="pfRisk__pf_risk_inherent_level", curie=ISO29100.curie('pf_risk_inherent_level'),
                   model_uri=ISO29100.pfRisk__pf_risk_inherent_level, domain=None, range=Optional[Union[str, "PfRiskLevel"]])

slots.pfRisk__pf_risk_residual_level = Slot(uri=ISO29100.pf_risk_residual_level, name="pfRisk__pf_risk_residual_level", curie=ISO29100.curie('pf_risk_residual_level'),
                   model_uri=ISO29100.pfRisk__pf_risk_residual_level, domain=None, range=Optional[Union[str, "PfRiskLevel"]])

slots.pfRisk__pf_risk_owner = Slot(uri=ISO29100.pf_risk_owner, name="pfRisk__pf_risk_owner", curie=ISO29100.curie('pf_risk_owner'),
                   model_uri=ISO29100.pfRisk__pf_risk_owner, domain=None, range=Optional[str])

slots.pfImpactAssessment__pf_assessment_scope = Slot(uri=ISO29100.pf_assessment_scope, name="pfImpactAssessment__pf_assessment_scope", curie=ISO29100.curie('pf_assessment_scope'),
                   model_uri=ISO29100.pfImpactAssessment__pf_assessment_scope, domain=None, range=Optional[str])

slots.pfImpactAssessment__pf_assessment_date = Slot(uri=ISO29100.pf_assessment_date, name="pfImpactAssessment__pf_assessment_date", curie=ISO29100.curie('pf_assessment_date'),
                   model_uri=ISO29100.pfImpactAssessment__pf_assessment_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.pfImpactAssessment__pf_assessor = Slot(uri=ISO29100.pf_assessor, name="pfImpactAssessment__pf_assessor", curie=ISO29100.curie('pf_assessor'),
                   model_uri=ISO29100.pfImpactAssessment__pf_assessor, domain=None, range=Optional[str])

slots.pfImpactAssessment__pf_assessed_activities = Slot(uri=ISO29100.pf_assessed_activities, name="pfImpactAssessment__pf_assessed_activities", curie=ISO29100.curie('pf_assessed_activities'),
                   model_uri=ISO29100.pfImpactAssessment__pf_assessed_activities, domain=None, range=Optional[Union[Union[str, PfProcessingActivityPfId], list[Union[str, PfProcessingActivityPfId]]]])

slots.pfImpactAssessment__pf_risks_found = Slot(uri=ISO29100.pf_risks_found, name="pfImpactAssessment__pf_risks_found", curie=ISO29100.curie('pf_risks_found'),
                   model_uri=ISO29100.pfImpactAssessment__pf_risks_found, domain=None, range=Optional[Union[Union[str, PfRiskPfId], list[Union[str, PfRiskPfId]]]])

slots.pfImpactAssessment__pf_risks_treated = Slot(uri=ISO29100.pf_risks_treated, name="pfImpactAssessment__pf_risks_treated", curie=ISO29100.curie('pf_risks_treated'),
                   model_uri=ISO29100.pfImpactAssessment__pf_risks_treated, domain=None, range=Optional[Union[Union[str, PfRiskPfId], list[Union[str, PfRiskPfId]]]])

slots.pfImpactAssessment__pf_risks_accepted = Slot(uri=ISO29100.pf_risks_accepted, name="pfImpactAssessment__pf_risks_accepted", curie=ISO29100.curie('pf_risks_accepted'),
                   model_uri=ISO29100.pfImpactAssessment__pf_risks_accepted, domain=None, range=Optional[Union[Union[str, PfRiskPfId], list[Union[str, PfRiskPfId]]]])

slots.pfImpactAssessment__pf_assessment_outcome = Slot(uri=ISO29100.pf_assessment_outcome, name="pfImpactAssessment__pf_assessment_outcome", curie=ISO29100.curie('pf_assessment_outcome'),
                   model_uri=ISO29100.pfImpactAssessment__pf_assessment_outcome, domain=None, range=Optional[str])

slots.pfImpactAssessment__pf_consultations = Slot(uri=ISO29100.pf_consultations, name="pfImpactAssessment__pf_consultations", curie=ISO29100.curie('pf_consultations'),
                   model_uri=ISO29100.pfImpactAssessment__pf_consultations, domain=None, range=Optional[Union[str, list[str]]])

slots.pfImpactAssessment__pf_next_assessment = Slot(uri=ISO29100.pf_next_assessment, name="pfImpactAssessment__pf_next_assessment", curie=ISO29100.curie('pf_next_assessment'),
                   model_uri=ISO29100.pfImpactAssessment__pf_next_assessment, domain=None, range=Optional[Union[str, XSDDate]])

slots.pfBreach__pf_breach_occurred = Slot(uri=ISO29100.pf_breach_occurred, name="pfBreach__pf_breach_occurred", curie=ISO29100.curie('pf_breach_occurred'),
                   model_uri=ISO29100.pfBreach__pf_breach_occurred, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.pfBreach__pf_breach_discovered = Slot(uri=ISO29100.pf_breach_discovered, name="pfBreach__pf_breach_discovered", curie=ISO29100.curie('pf_breach_discovered'),
                   model_uri=ISO29100.pfBreach__pf_breach_discovered, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.pfBreach__pf_breach_closed = Slot(uri=ISO29100.pf_breach_closed, name="pfBreach__pf_breach_closed", curie=ISO29100.curie('pf_breach_closed'),
                   model_uri=ISO29100.pfBreach__pf_breach_closed, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.pfBreach__pf_principals_affected = Slot(uri=ISO29100.pf_principals_affected, name="pfBreach__pf_principals_affected", curie=ISO29100.curie('pf_principals_affected'),
                   model_uri=ISO29100.pfBreach__pf_principals_affected, domain=None, range=Optional[int])

slots.pfBreach__pf_breached_requirements = Slot(uri=ISO29100.pf_breached_requirements, name="pfBreach__pf_breached_requirements", curie=ISO29100.curie('pf_breached_requirements'),
                   model_uri=ISO29100.pfBreach__pf_breached_requirements, domain=None, range=Optional[Union[Union[str, PfSafeguardingRequirementPfId], list[Union[str, PfSafeguardingRequirementPfId]]]])

slots.pfBreach__pf_breach_severity = Slot(uri=ISO29100.pf_breach_severity, name="pfBreach__pf_breach_severity", curie=ISO29100.curie('pf_breach_severity'),
                   model_uri=ISO29100.pfBreach__pf_breach_severity, domain=None, range=Optional[Union[str, "PfRiskLevel"]])

slots.pfBreach__pf_immediate_actions = Slot(uri=ISO29100.pf_immediate_actions, name="pfBreach__pf_immediate_actions", curie=ISO29100.curie('pf_immediate_actions'),
                   model_uri=ISO29100.pfBreach__pf_immediate_actions, domain=None, range=Optional[Union[str, list[str]]])

slots.pfBreach__pf_notification_required = Slot(uri=ISO29100.pf_notification_required, name="pfBreach__pf_notification_required", curie=ISO29100.curie('pf_notification_required'),
                   model_uri=ISO29100.pfBreach__pf_notification_required, domain=None, range=Optional[Union[bool, Bool]])

slots.pfBreach__pf_notifications = Slot(uri=ISO29100.pf_notifications, name="pfBreach__pf_notifications", curie=ISO29100.curie('pf_notifications'),
                   model_uri=ISO29100.pfBreach__pf_notifications, domain=None, range=Optional[Union[str, list[str]]])

slots.pfBreach__pf_remediation = Slot(uri=ISO29100.pf_remediation, name="pfBreach__pf_remediation", curie=ISO29100.curie('pf_remediation'),
                   model_uri=ISO29100.pfBreach__pf_remediation, domain=None, range=Optional[Union[str, list[str]]])

slots.pfBreach__pf_lessons = Slot(uri=ISO29100.pf_lessons, name="pfBreach__pf_lessons", curie=ISO29100.curie('pf_lessons'),
                   model_uri=ISO29100.pfBreach__pf_lessons, domain=None, range=Optional[str])

slots.pfConsent__pf_consent_mechanism = Slot(uri=ISO29100.pf_consent_mechanism, name="pfConsent__pf_consent_mechanism", curie=ISO29100.curie('pf_consent_mechanism'),
                   model_uri=ISO29100.pfConsent__pf_consent_mechanism, domain=None, range=Optional[Union[str, "PfConsentMechanism"]])

slots.pfConsent__pf_consent_given = Slot(uri=ISO29100.pf_consent_given, name="pfConsent__pf_consent_given", curie=ISO29100.curie('pf_consent_given'),
                   model_uri=ISO29100.pfConsent__pf_consent_given, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.pfConsent__pf_consent_state = Slot(uri=ISO29100.pf_consent_state, name="pfConsent__pf_consent_state", curie=ISO29100.curie('pf_consent_state'),
                   model_uri=ISO29100.pfConsent__pf_consent_state, domain=None, range=Union[str, "PfConsentState"])

slots.pfConsent__pf_consent_withdrawn = Slot(uri=ISO29100.pf_consent_withdrawn, name="pfConsent__pf_consent_withdrawn", curie=ISO29100.curie('pf_consent_withdrawn'),
                   model_uri=ISO29100.pfConsent__pf_consent_withdrawn, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.pfPreference__pf_preference_scope = Slot(uri=ISO29100.pf_preference_scope, name="pfPreference__pf_preference_scope", curie=ISO29100.curie('pf_preference_scope'),
                   model_uri=ISO29100.pfPreference__pf_preference_scope, domain=None, range=Optional[str])

slots.pfPreference__pf_wants_anonymity = Slot(uri=ISO29100.pf_wants_anonymity, name="pfPreference__pf_wants_anonymity", curie=ISO29100.curie('pf_wants_anonymity'),
                   model_uri=ISO29100.pfPreference__pf_wants_anonymity, domain=None, range=Optional[Union[bool, Bool]])

slots.pfPreference__pf_wants_pseudonymity = Slot(uri=ISO29100.pf_wants_pseudonymity, name="pfPreference__pf_wants_pseudonymity", curie=ISO29100.curie('pf_wants_pseudonymity'),
                   model_uri=ISO29100.pfPreference__pf_wants_pseudonymity, domain=None, range=Optional[Union[bool, Bool]])

slots.pfPreference__pf_refused_operations = Slot(uri=ISO29100.pf_refused_operations, name="pfPreference__pf_refused_operations", curie=ISO29100.curie('pf_refused_operations'),
                   model_uri=ISO29100.pfPreference__pf_refused_operations, domain=None, range=Optional[Union[Union[str, "PfOperation"], list[Union[str, "PfOperation"]]]])

slots.pfPreference__pf_refused_recipients = Slot(uri=ISO29100.pf_refused_recipients, name="pfPreference__pf_refused_recipients", curie=ISO29100.curie('pf_refused_recipients'),
                   model_uri=ISO29100.pfPreference__pf_refused_recipients, domain=None, range=Optional[Union[str, list[str]]])

slots.pfPreference__pf_preference_recorded = Slot(uri=ISO29100.pf_preference_recorded, name="pfPreference__pf_preference_recorded", curie=ISO29100.curie('pf_preference_recorded'),
                   model_uri=ISO29100.pfPreference__pf_preference_recorded, domain=None, range=Optional[Union[str, XSDDate]])

slots.PfRecordMixin_title = Slot(uri=SCHEMA.name, name="PfRecordMixin_title", curie=SCHEMA.curie('name'),
                   model_uri=ISO29100.PfRecordMixin_title, domain=None, range=str,
                   pattern=re.compile(r'^\s*\S'))

slots.PfActor_pf_actor_type = Slot(uri=ISO29100.pf_actor_type, name="PfActor_pf_actor_type", curie=ISO29100.curie('pf_actor_type'),
                   model_uri=ISO29100.PfActor_pf_actor_type, domain=PfActor, range=str)

slots.PfConsent_pf_principal = Slot(uri=ISO29100.pf_principal, name="PfConsent_pf_principal", curie=ISO29100.curie('pf_principal'),
                   model_uri=ISO29100.PfConsent_pf_principal, domain=PfConsent, range=Union[str, PfPiiPrincipalPfId])

slots.PfPreference_pf_principal = Slot(uri=ISO29100.pf_principal, name="PfPreference_pf_principal", curie=ISO29100.curie('pf_principal'),
                   model_uri=ISO29100.PfPreference_pf_principal, domain=PfPreference, range=Union[str, PfPiiPrincipalPfId])
