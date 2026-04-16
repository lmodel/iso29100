# Auto generated from iso29100.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-04-16T14:52:55
# Schema: iso29100
#
# id: https://w3id.org/lmodel/iso29100
# description: A comprehensive LinkML schema modeling the ISO/IEC 29100:2024 privacy framework for information and communication technology (ICT) systems. Captures actors and roles, PII recognition, privacy safeguarding requirements, the eleven privacy principles, and the privacy risk management process.
#   This schema covers: - Privacy framework actors (PII principal, controller, processor, third party) - Personally identifiable information (PII) and its categories - Privacy principles (11 principles from Clause 6) - Privacy safeguarding requirements and influencing factors - Privacy risk management including privacy impact assessment - Privacy policies, privacy controls, consent records, and privacy preferences
# license: https://www.apache.org/licenses/LICENSE-2.0

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

from linkml_runtime.linkml_model.types import Boolean, Date, Datetime, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, URIorCURIE, XSDDate, XSDDateTime

metamodel_version = "1.7.0"
version = "1.0.0"

# Namespaces
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
DPV = CurieNamespace('dpv', 'https://w3id.org/dpv#')
ISO27001 = CurieNamespace('iso27001', 'https://w3id.org/lmodel/iso27001/')
ISO29100 = CurieNamespace('iso29100', 'https://w3id.org/lmodel/iso29100/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = ISO29100


# Types
class PositiveIntegerType(int):
    """ Integer greater than zero; natural number explicitly excluding zero. """
    type_class_uri = XSD["positiveInteger"]
    type_class_curie = "xsd:positiveInteger"
    type_name = "positive_integer_type"
    type_model_uri = ISO29100.PositiveIntegerType


class DurationType(str):
    """ ISO 8601 duration value such as P1Y, P30D, or PT4H. """
    type_class_uri = XSD["duration"]
    type_class_curie = "xsd:duration"
    type_name = "duration_type"
    type_model_uri = ISO29100.DurationType


# Class references
class NamedEntityId(URIorCURIE):
    pass


class PrivacyFrameworkId(NamedEntityId):
    pass


class PrivacyStakeholderId(NamedEntityId):
    pass


class PIIPrincipalId(PrivacyStakeholderId):
    pass


class PIIControllerId(PrivacyStakeholderId):
    pass


class PIIProcessorId(PrivacyStakeholderId):
    pass


class ThirdPartyId(PrivacyStakeholderId):
    pass


class PersonallyIdentifiableInformationId(NamedEntityId):
    pass


class PIIFlowScenarioId(NamedEntityId):
    pass


class PrivacySafeguardingRequirementId(NamedEntityId):
    pass


class PrivacyPolicyId(NamedEntityId):
    pass


class PrivacyControlId(NamedEntityId):
    pass


class PrivacyRiskId(NamedEntityId):
    pass


class PrivacyImpactAssessmentId(NamedEntityId):
    pass


class PrivacyBreachId(NamedEntityId):
    pass


class PIIProcessingActivityId(NamedEntityId):
    pass


class PrivacyPrincipleImplementationId(NamedEntityId):
    pass


class ConsentRecordId(NamedEntityId):
    pass


class PrivacyPreferenceId(NamedEntityId):
    pass


@dataclass(repr=False)
class NamedEntity(YAMLRoot):
    """
    Abstract base class for all entities with a unique identifier, name, and description. Provides common
    identification and documentation slots.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO29100["NamedEntity"]
    class_class_curie: ClassVar[str] = "iso29100:NamedEntity"
    class_name: ClassVar[str] = "NamedEntity"
    class_model_uri: ClassVar[URIRef] = ISO29100.NamedEntity

    id: Union[str, NamedEntityId] = None
    name: str = None
    description: Optional[str] = None
    created_date: Optional[Union[str, XSDDate]] = None
    modified_date: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedEntityId):
            self.id = NamedEntityId(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.created_date is not None and not isinstance(self.created_date, XSDDate):
            self.created_date = XSDDate(self.created_date)

        if self.modified_date is not None and not isinstance(self.modified_date, XSDDate):
            self.modified_date = XSDDate(self.modified_date)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PrivacyFramework(NamedEntity):
    """
    Top-level container representing an organization's privacy framework for protecting PII within ICT systems.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO29100["PrivacyFramework"]
    class_class_curie: ClassVar[str] = "iso29100:PrivacyFramework"
    class_name: ClassVar[str] = "PrivacyFramework"
    class_model_uri: ClassVar[URIRef] = ISO29100.PrivacyFramework

    id: Union[str, PrivacyFrameworkId] = None
    name: str = None
    organization_name: Optional[str] = None
    ict_system_description: Optional[str] = None
    applicable_jurisdictions: Optional[Union[str, list[str]]] = empty_list()
    pii_controllers: Optional[Union[dict[Union[str, PIIControllerId], Union[dict, "PIIController"]], list[Union[dict, "PIIController"]]]] = empty_dict()
    pii_processors: Optional[Union[dict[Union[str, PIIProcessorId], Union[dict, "PIIProcessor"]], list[Union[dict, "PIIProcessor"]]]] = empty_dict()
    third_parties: Optional[Union[dict[Union[str, ThirdPartyId], Union[dict, "ThirdParty"]], list[Union[dict, "ThirdParty"]]]] = empty_dict()
    pii_principals_description: Optional[str] = None
    privacy_policy: Optional[Union[str, PrivacyPolicyId]] = None
    privacy_controls: Optional[Union[dict[Union[str, PrivacyControlId], Union[dict, "PrivacyControl"]], list[Union[dict, "PrivacyControl"]]]] = empty_dict()
    safeguarding_requirements: Optional[Union[dict[Union[str, PrivacySafeguardingRequirementId], Union[dict, "PrivacySafeguardingRequirement"]], list[Union[dict, "PrivacySafeguardingRequirement"]]]] = empty_dict()
    privacy_risks: Optional[Union[dict[Union[str, PrivacyRiskId], Union[dict, "PrivacyRisk"]], list[Union[dict, "PrivacyRisk"]]]] = empty_dict()
    privacy_impact_assessments: Optional[Union[dict[Union[str, PrivacyImpactAssessmentId], Union[dict, "PrivacyImpactAssessment"]], list[Union[dict, "PrivacyImpactAssessment"]]]] = empty_dict()
    privacy_breaches: Optional[Union[dict[Union[str, PrivacyBreachId], Union[dict, "PrivacyBreach"]], list[Union[dict, "PrivacyBreach"]]]] = empty_dict()
    pii_processing_activities: Optional[Union[dict[Union[str, PIIProcessingActivityId], Union[dict, "PIIProcessingActivity"]], list[Union[dict, "PIIProcessingActivity"]]]] = empty_dict()
    principle_implementations: Optional[Union[dict[Union[str, PrivacyPrincipleImplementationId], Union[dict, "PrivacyPrincipleImplementation"]], list[Union[dict, "PrivacyPrincipleImplementation"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PrivacyFrameworkId):
            self.id = PrivacyFrameworkId(self.id)

        if self.organization_name is not None and not isinstance(self.organization_name, str):
            self.organization_name = str(self.organization_name)

        if self.ict_system_description is not None and not isinstance(self.ict_system_description, str):
            self.ict_system_description = str(self.ict_system_description)

        if not isinstance(self.applicable_jurisdictions, list):
            self.applicable_jurisdictions = [self.applicable_jurisdictions] if self.applicable_jurisdictions is not None else []
        self.applicable_jurisdictions = [v if isinstance(v, str) else str(v) for v in self.applicable_jurisdictions]

        self._normalize_inlined_as_list(slot_name="pii_controllers", slot_type=PIIController, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="pii_processors", slot_type=PIIProcessor, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="third_parties", slot_type=ThirdParty, key_name="id", keyed=True)

        if self.pii_principals_description is not None and not isinstance(self.pii_principals_description, str):
            self.pii_principals_description = str(self.pii_principals_description)

        if self.privacy_policy is not None and not isinstance(self.privacy_policy, PrivacyPolicyId):
            self.privacy_policy = PrivacyPolicyId(self.privacy_policy)

        self._normalize_inlined_as_list(slot_name="privacy_controls", slot_type=PrivacyControl, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="safeguarding_requirements", slot_type=PrivacySafeguardingRequirement, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="privacy_risks", slot_type=PrivacyRisk, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="privacy_impact_assessments", slot_type=PrivacyImpactAssessment, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="privacy_breaches", slot_type=PrivacyBreach, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="pii_processing_activities", slot_type=PIIProcessingActivity, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="principle_implementations", slot_type=PrivacyPrincipleImplementation, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PrivacyStakeholder(NamedEntity):
    """
    Schema base class for the four actor types recognized by the privacy framework: PII principals, PII controllers,
    PII processors, and third parties. Provides shared contact and jurisdictional attributes common to all stakeholder
    roles.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO29100["PrivacyStakeholder"]
    class_class_curie: ClassVar[str] = "iso29100:PrivacyStakeholder"
    class_name: ClassVar[str] = "PrivacyStakeholder"
    class_model_uri: ClassVar[URIRef] = ISO29100.PrivacyStakeholder

    id: Union[str, PrivacyStakeholderId] = None
    name: str = None
    contact_information: Optional[str] = None
    jurisdictions: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.contact_information is not None and not isinstance(self.contact_information, str):
            self.contact_information = str(self.contact_information)

        if not isinstance(self.jurisdictions, list):
            self.jurisdictions = [self.jurisdictions] if self.jurisdictions is not None else []
        self.jurisdictions = [v if isinstance(v, str) else str(v) for v in self.jurisdictions]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PIIPrincipal(PrivacyStakeholder):
    """
    Schema class for a data subject — the individual to whom PII belongs. Links consent records and privacy
    preferences to the natural person whose data is being processed, enabling subject-centric data models.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO29100["PIIPrincipal"]
    class_class_curie: ClassVar[str] = "iso29100:PIIPrincipal"
    class_name: ClassVar[str] = "PIIPrincipal"
    class_model_uri: ClassVar[URIRef] = ISO29100.PIIPrincipal

    id: Union[str, PIIPrincipalId] = None
    name: str = None
    privacy_preferences: Optional[Union[dict[Union[str, PrivacyPreferenceId], Union[dict, "PrivacyPreference"]], list[Union[dict, "PrivacyPreference"]]]] = empty_dict()
    consent_records: Optional[Union[dict[Union[str, ConsentRecordId], Union[dict, "ConsentRecord"]], list[Union[dict, "ConsentRecord"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PIIPrincipalId):
            self.id = PIIPrincipalId(self.id)

        self._normalize_inlined_as_list(slot_name="privacy_preferences", slot_type=PrivacyPreference, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="consent_records", slot_type=ConsentRecord, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PIIController(PrivacyStakeholder):
    """
    Schema class for an organization or individual that determines why and how PII is processed. Captures appointed
    processors, legal bases relied upon, privacy policy reference, and data protection officer details. Bears ultimate
    accountability for privacy principle adherence.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO29100["PIIController"]
    class_class_curie: ClassVar[str] = "iso29100:PIIController"
    class_name: ClassVar[str] = "PIIController"
    class_model_uri: ClassVar[URIRef] = ISO29100.PIIController

    id: Union[str, PIIControllerId] = None
    name: str = None
    processing_purposes: Optional[Union[str, list[str]]] = empty_list()
    legal_bases: Optional[Union[str, list[str]]] = empty_list()
    appointed_processors: Optional[Union[Union[str, PIIProcessorId], list[Union[str, PIIProcessorId]]]] = empty_list()
    privacy_policy_ref: Optional[Union[str, PrivacyPolicyId]] = None
    data_protection_officer: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PIIControllerId):
            self.id = PIIControllerId(self.id)

        if not isinstance(self.processing_purposes, list):
            self.processing_purposes = [self.processing_purposes] if self.processing_purposes is not None else []
        self.processing_purposes = [v if isinstance(v, str) else str(v) for v in self.processing_purposes]

        if not isinstance(self.legal_bases, list):
            self.legal_bases = [self.legal_bases] if self.legal_bases is not None else []
        self.legal_bases = [v if isinstance(v, str) else str(v) for v in self.legal_bases]

        if not isinstance(self.appointed_processors, list):
            self.appointed_processors = [self.appointed_processors] if self.appointed_processors is not None else []
        self.appointed_processors = [v if isinstance(v, PIIProcessorId) else PIIProcessorId(v) for v in self.appointed_processors]

        if self.privacy_policy_ref is not None and not isinstance(self.privacy_policy_ref, PrivacyPolicyId):
            self.privacy_policy_ref = PrivacyPolicyId(self.privacy_policy_ref)

        if self.data_protection_officer is not None and not isinstance(self.data_protection_officer, str):
            self.data_protection_officer = str(self.data_protection_officer)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PIIProcessor(PrivacyStakeholder):
    """
    Schema class for an organization engaged to process PII under a PII controller's instructions. Records the
    instructing controller, data processing agreement reference, and any sub-processors engaged on the controller's
    behalf.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO29100["PIIProcessor"]
    class_class_curie: ClassVar[str] = "iso29100:PIIProcessor"
    class_name: ClassVar[str] = "PIIProcessor"
    class_model_uri: ClassVar[URIRef] = ISO29100.PIIProcessor

    id: Union[str, PIIProcessorId] = None
    name: str = None
    instructing_controller: Optional[Union[str, PIIControllerId]] = None
    processing_agreement_ref: Optional[str] = None
    sub_processors: Optional[Union[Union[str, PIIProcessorId], list[Union[str, PIIProcessorId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PIIProcessorId):
            self.id = PIIProcessorId(self.id)

        if self.instructing_controller is not None and not isinstance(self.instructing_controller, PIIControllerId):
            self.instructing_controller = PIIControllerId(self.instructing_controller)

        if self.processing_agreement_ref is not None and not isinstance(self.processing_agreement_ref, str):
            self.processing_agreement_ref = str(self.processing_agreement_ref)

        if not isinstance(self.sub_processors, list):
            self.sub_processors = [self.sub_processors] if self.sub_processors is not None else []
        self.sub_processors = [v if isinstance(v, PIIProcessorId) else PIIProcessorId(v) for v in self.sub_processors]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ThirdParty(PrivacyStakeholder):
    """
    Schema class for an external entity that receives PII outside the PII processor relationship — i.e., as a
    recipient that typically becomes a PII controller in its own right. Captures the receiving purpose and the legal
    basis for the transfer.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO29100["ThirdParty"]
    class_class_curie: ClassVar[str] = "iso29100:ThirdParty"
    class_name: ClassVar[str] = "ThirdParty"
    class_model_uri: ClassVar[URIRef] = ISO29100.ThirdParty

    id: Union[str, ThirdPartyId] = None
    name: str = None
    receiving_purpose: Optional[str] = None
    transfer_basis: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ThirdPartyId):
            self.id = ThirdPartyId(self.id)

        if self.receiving_purpose is not None and not isinstance(self.receiving_purpose, str):
            self.receiving_purpose = str(self.receiving_purpose)

        if self.transfer_basis is not None and not isinstance(self.transfer_basis, str):
            self.transfer_basis = str(self.transfer_basis)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PersonallyIdentifiableInformation(NamedEntity):
    """
    Schema class representing a data element or attribute set that can be linked back to a natural person — either
    directly or through combination with other attributes. Captures sensitivity classification, identifier type,
    pseudonymization status, retention schedule, and processing operations applicable to the data.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO29100["PersonallyIdentifiableInformation"]
    class_class_curie: ClassVar[str] = "iso29100:PersonallyIdentifiableInformation"
    class_name: ClassVar[str] = "PersonallyIdentifiableInformation"
    class_model_uri: ClassVar[URIRef] = ISO29100.PersonallyIdentifiableInformation

    id: Union[str, PersonallyIdentifiableInformationId] = None
    name: str = None
    pii_category: Optional[Union[str, list[str]]] = empty_list()
    sensitivity_level: Optional[Union[str, "PIISensitivityCategory"]] = None
    identifier_type: Optional[str] = None
    is_pseudonymized: Optional[Union[bool, Bool]] = None
    is_anonymized: Optional[Union[bool, Bool]] = None
    linkability_risk: Optional[str] = None
    applicable_to_principal: Optional[str] = None
    retention_schedule: Optional[str] = None
    processing_operations: Optional[Union[Union[str, "PIIProcessingOperation"], list[Union[str, "PIIProcessingOperation"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PersonallyIdentifiableInformationId):
            self.id = PersonallyIdentifiableInformationId(self.id)

        if not isinstance(self.pii_category, list):
            self.pii_category = [self.pii_category] if self.pii_category is not None else []
        self.pii_category = [v if isinstance(v, str) else str(v) for v in self.pii_category]

        if self.sensitivity_level is not None and not isinstance(self.sensitivity_level, PIISensitivityCategory):
            self.sensitivity_level = PIISensitivityCategory(self.sensitivity_level)

        if self.identifier_type is not None and not isinstance(self.identifier_type, str):
            self.identifier_type = str(self.identifier_type)

        if self.is_pseudonymized is not None and not isinstance(self.is_pseudonymized, Bool):
            self.is_pseudonymized = Bool(self.is_pseudonymized)

        if self.is_anonymized is not None and not isinstance(self.is_anonymized, Bool):
            self.is_anonymized = Bool(self.is_anonymized)

        if self.linkability_risk is not None and not isinstance(self.linkability_risk, str):
            self.linkability_risk = str(self.linkability_risk)

        if self.applicable_to_principal is not None and not isinstance(self.applicable_to_principal, str):
            self.applicable_to_principal = str(self.applicable_to_principal)

        if self.retention_schedule is not None and not isinstance(self.retention_schedule, str):
            self.retention_schedule = str(self.retention_schedule)

        if not isinstance(self.processing_operations, list):
            self.processing_operations = [self.processing_operations] if self.processing_operations is not None else []
        self.processing_operations = [v if isinstance(v, PIIProcessingOperation) else PIIProcessingOperation(v) for v in self.processing_operations]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PIIFlowScenario(NamedEntity):
    """
    A documented scenario describing the flow of PII among privacy framework actors (PII principal, PII controller,
    PII processor, and third party), as illustrated in Table 1 of Clause 5.3.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO29100["PIIFlowScenario"]
    class_class_curie: ClassVar[str] = "iso29100:PIIFlowScenario"
    class_name: ClassVar[str] = "PIIFlowScenario"
    class_model_uri: ClassVar[URIRef] = ISO29100.PIIFlowScenario

    id: Union[str, PIIFlowScenarioId] = None
    name: str = None
    scenario_label: Optional[str] = None
    pii_principal_role: Optional[Union[str, "PIIFlowRole"]] = None
    pii_controller_role: Optional[Union[str, "PIIFlowRole"]] = None
    pii_processor_role: Optional[Union[str, "PIIFlowRole"]] = None
    third_party_role: Optional[Union[str, "PIIFlowRole"]] = None
    scenario_description: Optional[str] = None
    legal_control_retention: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PIIFlowScenarioId):
            self.id = PIIFlowScenarioId(self.id)

        if self.scenario_label is not None and not isinstance(self.scenario_label, str):
            self.scenario_label = str(self.scenario_label)

        if self.pii_principal_role is not None and not isinstance(self.pii_principal_role, PIIFlowRole):
            self.pii_principal_role = PIIFlowRole(self.pii_principal_role)

        if self.pii_controller_role is not None and not isinstance(self.pii_controller_role, PIIFlowRole):
            self.pii_controller_role = PIIFlowRole(self.pii_controller_role)

        if self.pii_processor_role is not None and not isinstance(self.pii_processor_role, PIIFlowRole):
            self.pii_processor_role = PIIFlowRole(self.pii_processor_role)

        if self.third_party_role is not None and not isinstance(self.third_party_role, PIIFlowRole):
            self.third_party_role = PIIFlowRole(self.third_party_role)

        if self.scenario_description is not None and not isinstance(self.scenario_description, str):
            self.scenario_description = str(self.scenario_description)

        if self.legal_control_retention is not None and not isinstance(self.legal_control_retention, str):
            self.legal_control_retention = str(self.legal_control_retention)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PrivacySafeguardingRequirement(NamedEntity):
    """
    Schema class for an applicable requirement that drives an organization's PII processing controls. Requirements are
    identified through the privacy risk management process and arise from legal/regulatory, contractual, business, or
    other influencing factors.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO29100["PrivacySafeguardingRequirement"]
    class_class_curie: ClassVar[str] = "iso29100:PrivacySafeguardingRequirement"
    class_name: ClassVar[str] = "PrivacySafeguardingRequirement"
    class_model_uri: ClassVar[URIRef] = ISO29100.PrivacySafeguardingRequirement

    id: Union[str, PrivacySafeguardingRequirementId] = None
    name: str = None
    requirement_factor: Optional[Union[str, "SafeguardingRequirementFactor"]] = None
    requirement_text: Optional[str] = None
    source_reference: Optional[str] = None
    applicable_to_actors: Optional[Union[str, list[str]]] = empty_list()
    related_controls: Optional[Union[Union[str, PrivacyControlId], list[Union[str, PrivacyControlId]]]] = empty_list()
    priority: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PrivacySafeguardingRequirementId):
            self.id = PrivacySafeguardingRequirementId(self.id)

        if self.requirement_factor is not None and not isinstance(self.requirement_factor, SafeguardingRequirementFactor):
            self.requirement_factor = SafeguardingRequirementFactor(self.requirement_factor)

        if self.requirement_text is not None and not isinstance(self.requirement_text, str):
            self.requirement_text = str(self.requirement_text)

        if self.source_reference is not None and not isinstance(self.source_reference, str):
            self.source_reference = str(self.source_reference)

        if not isinstance(self.applicable_to_actors, list):
            self.applicable_to_actors = [self.applicable_to_actors] if self.applicable_to_actors is not None else []
        self.applicable_to_actors = [v if isinstance(v, str) else str(v) for v in self.applicable_to_actors]

        if not isinstance(self.related_controls, list):
            self.related_controls = [self.related_controls] if self.related_controls is not None else []
        self.related_controls = [v if isinstance(v, PrivacyControlId) else PrivacyControlId(v) for v in self.related_controls]

        if self.priority is not None and not isinstance(self.priority, str):
            self.priority = str(self.priority)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PrivacyPolicy(NamedEntity):
    """
    Schema class for a governing document expressing an organization's intentions and commitments for PII processing.
    Covers both the internal policy document and any external privacy notice made available to PII principals
    (referred to as a notice in this framework).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO29100["PrivacyPolicy"]
    class_class_curie: ClassVar[str] = "iso29100:PrivacyPolicy"
    class_name: ClassVar[str] = "PrivacyPolicy"
    class_model_uri: ClassVar[URIRef] = ISO29100.PrivacyPolicy

    id: Union[str, PrivacyPolicyId] = None
    name: str = None
    policy_version: Optional[str] = None
    effective_date: Optional[Union[str, XSDDate]] = None
    policy_scope: Optional[str] = None
    processing_purposes_covered: Optional[Union[str, list[str]]] = empty_list()
    pii_categories_covered: Optional[Union[str, list[str]]] = empty_list()
    data_retention_statement: Optional[str] = None
    pii_principal_rights: Optional[Union[str, list[str]]] = empty_list()
    contact_for_inquiries: Optional[str] = None
    last_review_date: Optional[Union[str, XSDDate]] = None
    is_external_notice: Optional[Union[bool, Bool]] = None
    applicable_principles: Optional[Union[Union[str, "PrivacyPrinciple"], list[Union[str, "PrivacyPrinciple"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PrivacyPolicyId):
            self.id = PrivacyPolicyId(self.id)

        if self.policy_version is not None and not isinstance(self.policy_version, str):
            self.policy_version = str(self.policy_version)

        if self.effective_date is not None and not isinstance(self.effective_date, XSDDate):
            self.effective_date = XSDDate(self.effective_date)

        if self.policy_scope is not None and not isinstance(self.policy_scope, str):
            self.policy_scope = str(self.policy_scope)

        if not isinstance(self.processing_purposes_covered, list):
            self.processing_purposes_covered = [self.processing_purposes_covered] if self.processing_purposes_covered is not None else []
        self.processing_purposes_covered = [v if isinstance(v, str) else str(v) for v in self.processing_purposes_covered]

        if not isinstance(self.pii_categories_covered, list):
            self.pii_categories_covered = [self.pii_categories_covered] if self.pii_categories_covered is not None else []
        self.pii_categories_covered = [v if isinstance(v, str) else str(v) for v in self.pii_categories_covered]

        if self.data_retention_statement is not None and not isinstance(self.data_retention_statement, str):
            self.data_retention_statement = str(self.data_retention_statement)

        if not isinstance(self.pii_principal_rights, list):
            self.pii_principal_rights = [self.pii_principal_rights] if self.pii_principal_rights is not None else []
        self.pii_principal_rights = [v if isinstance(v, str) else str(v) for v in self.pii_principal_rights]

        if self.contact_for_inquiries is not None and not isinstance(self.contact_for_inquiries, str):
            self.contact_for_inquiries = str(self.contact_for_inquiries)

        if self.last_review_date is not None and not isinstance(self.last_review_date, XSDDate):
            self.last_review_date = XSDDate(self.last_review_date)

        if self.is_external_notice is not None and not isinstance(self.is_external_notice, Bool):
            self.is_external_notice = Bool(self.is_external_notice)

        if not isinstance(self.applicable_principles, list):
            self.applicable_principles = [self.applicable_principles] if self.applicable_principles is not None else []
        self.applicable_principles = [v if isinstance(v, PrivacyPrinciple) else PrivacyPrinciple(v) for v in self.applicable_principles]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PrivacyControl(NamedEntity):
    """
    Schema class for a protective measure that manages privacy risks within the framework. Can be organizational,
    physical, technical (including Privacy Enhancing Technologies), or legal-contractual in nature; linked to the
    principles and safeguarding requirements it addresses.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO29100["PrivacyControl"]
    class_class_curie: ClassVar[str] = "iso29100:PrivacyControl"
    class_name: ClassVar[str] = "PrivacyControl"
    class_model_uri: ClassVar[URIRef] = ISO29100.PrivacyControl

    id: Union[str, PrivacyControlId] = None
    name: str = None
    control_type: Optional[Union[str, "PrivacyControlType"]] = None
    control_objective: Optional[str] = None
    addressed_principles: Optional[Union[Union[str, "PrivacyPrinciple"], list[Union[str, "PrivacyPrinciple"]]]] = empty_list()
    implementation_description: Optional[str] = None
    responsible_actor: Optional[str] = None
    implementation_status: Optional[str] = None
    effectiveness_evidence: Optional[Union[str, list[str]]] = empty_list()
    related_safeguarding_requirements: Optional[Union[Union[str, PrivacySafeguardingRequirementId], list[Union[str, PrivacySafeguardingRequirementId]]]] = empty_list()
    is_pet: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PrivacyControlId):
            self.id = PrivacyControlId(self.id)

        if self.control_type is not None and not isinstance(self.control_type, PrivacyControlType):
            self.control_type = PrivacyControlType(self.control_type)

        if self.control_objective is not None and not isinstance(self.control_objective, str):
            self.control_objective = str(self.control_objective)

        if not isinstance(self.addressed_principles, list):
            self.addressed_principles = [self.addressed_principles] if self.addressed_principles is not None else []
        self.addressed_principles = [v if isinstance(v, PrivacyPrinciple) else PrivacyPrinciple(v) for v in self.addressed_principles]

        if self.implementation_description is not None and not isinstance(self.implementation_description, str):
            self.implementation_description = str(self.implementation_description)

        if self.responsible_actor is not None and not isinstance(self.responsible_actor, str):
            self.responsible_actor = str(self.responsible_actor)

        if self.implementation_status is not None and not isinstance(self.implementation_status, str):
            self.implementation_status = str(self.implementation_status)

        if not isinstance(self.effectiveness_evidence, list):
            self.effectiveness_evidence = [self.effectiveness_evidence] if self.effectiveness_evidence is not None else []
        self.effectiveness_evidence = [v if isinstance(v, str) else str(v) for v in self.effectiveness_evidence]

        if not isinstance(self.related_safeguarding_requirements, list):
            self.related_safeguarding_requirements = [self.related_safeguarding_requirements] if self.related_safeguarding_requirements is not None else []
        self.related_safeguarding_requirements = [v if isinstance(v, PrivacySafeguardingRequirementId) else PrivacySafeguardingRequirementId(v) for v in self.related_safeguarding_requirements]

        if self.is_pet is not None and not isinstance(self.is_pet, Bool):
            self.is_pet = Bool(self.is_pet)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PrivacyRisk(NamedEntity):
    """
    Schema class representing a potential adverse outcome for PII principals from a PII processing activity. Captures
    the risk source, likelihood and impact assessments, inherent and residual risk levels, and links to mitigating
    controls and accountable risk owner.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO29100["PrivacyRisk"]
    class_class_curie: ClassVar[str] = "iso29100:PrivacyRisk"
    class_name: ClassVar[str] = "PrivacyRisk"
    class_model_uri: ClassVar[URIRef] = ISO29100.PrivacyRisk

    id: Union[str, PrivacyRiskId] = None
    name: str = None
    risk_source: Optional[str] = None
    affected_pii_categories: Optional[Union[str, list[str]]] = empty_list()
    affected_principals_description: Optional[str] = None
    risk_likelihood: Optional[str] = None
    risk_impact_description: Optional[str] = None
    inherent_risk_level: Optional[Union[str, "PrivacyRiskLevel"]] = None
    residual_risk_level: Optional[Union[str, "PrivacyRiskLevel"]] = None
    mitigating_controls: Optional[Union[Union[str, PrivacyControlId], list[Union[str, PrivacyControlId]]]] = empty_list()
    risk_owner: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PrivacyRiskId):
            self.id = PrivacyRiskId(self.id)

        if self.risk_source is not None and not isinstance(self.risk_source, str):
            self.risk_source = str(self.risk_source)

        if not isinstance(self.affected_pii_categories, list):
            self.affected_pii_categories = [self.affected_pii_categories] if self.affected_pii_categories is not None else []
        self.affected_pii_categories = [v if isinstance(v, str) else str(v) for v in self.affected_pii_categories]

        if self.affected_principals_description is not None and not isinstance(self.affected_principals_description, str):
            self.affected_principals_description = str(self.affected_principals_description)

        if self.risk_likelihood is not None and not isinstance(self.risk_likelihood, str):
            self.risk_likelihood = str(self.risk_likelihood)

        if self.risk_impact_description is not None and not isinstance(self.risk_impact_description, str):
            self.risk_impact_description = str(self.risk_impact_description)

        if self.inherent_risk_level is not None and not isinstance(self.inherent_risk_level, PrivacyRiskLevel):
            self.inherent_risk_level = PrivacyRiskLevel(self.inherent_risk_level)

        if self.residual_risk_level is not None and not isinstance(self.residual_risk_level, PrivacyRiskLevel):
            self.residual_risk_level = PrivacyRiskLevel(self.residual_risk_level)

        if not isinstance(self.mitigating_controls, list):
            self.mitigating_controls = [self.mitigating_controls] if self.mitigating_controls is not None else []
        self.mitigating_controls = [v if isinstance(v, PrivacyControlId) else PrivacyControlId(v) for v in self.mitigating_controls]

        if self.risk_owner is not None and not isinstance(self.risk_owner, str):
            self.risk_owner = str(self.risk_owner)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PrivacyImpactAssessment(NamedEntity):
    """
    Schema class for a structured evaluation of the privacy implications of a processing activity or ICT system.
    Records assessment scope, identified and treated risks, accepted residual risks, stakeholder consultation records,
    and overall assessment outcome.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO29100["PrivacyImpactAssessment"]
    class_class_curie: ClassVar[str] = "iso29100:PrivacyImpactAssessment"
    class_name: ClassVar[str] = "PrivacyImpactAssessment"
    class_model_uri: ClassVar[URIRef] = ISO29100.PrivacyImpactAssessment

    id: Union[str, PrivacyImpactAssessmentId] = None
    name: str = None
    assessment_scope: Optional[str] = None
    assessment_date: Optional[Union[str, XSDDate]] = None
    assessor: Optional[str] = None
    processing_activities_assessed: Optional[Union[Union[str, PIIProcessingActivityId], list[Union[str, PIIProcessingActivityId]]]] = empty_list()
    risks_identified: Optional[Union[Union[str, PrivacyRiskId], list[Union[str, PrivacyRiskId]]]] = empty_list()
    risks_treated: Optional[Union[Union[str, PrivacyRiskId], list[Union[str, PrivacyRiskId]]]] = empty_list()
    residual_risks_accepted: Optional[Union[Union[str, PrivacyRiskId], list[Union[str, PrivacyRiskId]]]] = empty_list()
    assessment_outcome: Optional[str] = None
    next_assessment_date: Optional[Union[str, XSDDate]] = None
    consultation_records: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PrivacyImpactAssessmentId):
            self.id = PrivacyImpactAssessmentId(self.id)

        if self.assessment_scope is not None and not isinstance(self.assessment_scope, str):
            self.assessment_scope = str(self.assessment_scope)

        if self.assessment_date is not None and not isinstance(self.assessment_date, XSDDate):
            self.assessment_date = XSDDate(self.assessment_date)

        if self.assessor is not None and not isinstance(self.assessor, str):
            self.assessor = str(self.assessor)

        if not isinstance(self.processing_activities_assessed, list):
            self.processing_activities_assessed = [self.processing_activities_assessed] if self.processing_activities_assessed is not None else []
        self.processing_activities_assessed = [v if isinstance(v, PIIProcessingActivityId) else PIIProcessingActivityId(v) for v in self.processing_activities_assessed]

        if not isinstance(self.risks_identified, list):
            self.risks_identified = [self.risks_identified] if self.risks_identified is not None else []
        self.risks_identified = [v if isinstance(v, PrivacyRiskId) else PrivacyRiskId(v) for v in self.risks_identified]

        if not isinstance(self.risks_treated, list):
            self.risks_treated = [self.risks_treated] if self.risks_treated is not None else []
        self.risks_treated = [v if isinstance(v, PrivacyRiskId) else PrivacyRiskId(v) for v in self.risks_treated]

        if not isinstance(self.residual_risks_accepted, list):
            self.residual_risks_accepted = [self.residual_risks_accepted] if self.residual_risks_accepted is not None else []
        self.residual_risks_accepted = [v if isinstance(v, PrivacyRiskId) else PrivacyRiskId(v) for v in self.residual_risks_accepted]

        if self.assessment_outcome is not None and not isinstance(self.assessment_outcome, str):
            self.assessment_outcome = str(self.assessment_outcome)

        if self.next_assessment_date is not None and not isinstance(self.next_assessment_date, XSDDate):
            self.next_assessment_date = XSDDate(self.next_assessment_date)

        if not isinstance(self.consultation_records, list):
            self.consultation_records = [self.consultation_records] if self.consultation_records is not None else []
        self.consultation_records = [v if isinstance(v, str) else str(v) for v in self.consultation_records]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PrivacyBreach(NamedEntity):
    """
    Schema class for a recorded incident in which PII was processed in a manner that violates applicable privacy
    safeguarding requirements. Tracks breach details, affected PII categories, notification obligations, remediation
    actions, and lessons learned.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO29100["PrivacyBreach"]
    class_class_curie: ClassVar[str] = "iso29100:PrivacyBreach"
    class_name: ClassVar[str] = "PrivacyBreach"
    class_model_uri: ClassVar[URIRef] = ISO29100.PrivacyBreach

    id: Union[str, PrivacyBreachId] = None
    name: str = None
    breach_datetime: Optional[Union[str, XSDDateTime]] = None
    discovery_datetime: Optional[Union[str, XSDDateTime]] = None
    breach_description: Optional[str] = None
    affected_pii_categories: Optional[Union[str, list[str]]] = empty_list()
    affected_principals_count: Optional[int] = None
    violated_requirements: Optional[Union[Union[str, PrivacySafeguardingRequirementId], list[Union[str, PrivacySafeguardingRequirementId]]]] = empty_list()
    breach_severity: Optional[Union[str, "PrivacyRiskLevel"]] = None
    immediate_actions: Optional[Union[str, list[str]]] = empty_list()
    notification_required: Optional[Union[bool, Bool]] = None
    notifications_made: Optional[Union[str, list[str]]] = empty_list()
    remediation_actions: Optional[Union[str, list[str]]] = empty_list()
    lessons_learned: Optional[str] = None
    closure_datetime: Optional[Union[str, XSDDateTime]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PrivacyBreachId):
            self.id = PrivacyBreachId(self.id)

        if self.breach_datetime is not None and not isinstance(self.breach_datetime, XSDDateTime):
            self.breach_datetime = XSDDateTime(self.breach_datetime)

        if self.discovery_datetime is not None and not isinstance(self.discovery_datetime, XSDDateTime):
            self.discovery_datetime = XSDDateTime(self.discovery_datetime)

        if self.breach_description is not None and not isinstance(self.breach_description, str):
            self.breach_description = str(self.breach_description)

        if not isinstance(self.affected_pii_categories, list):
            self.affected_pii_categories = [self.affected_pii_categories] if self.affected_pii_categories is not None else []
        self.affected_pii_categories = [v if isinstance(v, str) else str(v) for v in self.affected_pii_categories]

        if self.affected_principals_count is not None and not isinstance(self.affected_principals_count, int):
            self.affected_principals_count = int(self.affected_principals_count)

        if not isinstance(self.violated_requirements, list):
            self.violated_requirements = [self.violated_requirements] if self.violated_requirements is not None else []
        self.violated_requirements = [v if isinstance(v, PrivacySafeguardingRequirementId) else PrivacySafeguardingRequirementId(v) for v in self.violated_requirements]

        if self.breach_severity is not None and not isinstance(self.breach_severity, PrivacyRiskLevel):
            self.breach_severity = PrivacyRiskLevel(self.breach_severity)

        if not isinstance(self.immediate_actions, list):
            self.immediate_actions = [self.immediate_actions] if self.immediate_actions is not None else []
        self.immediate_actions = [v if isinstance(v, str) else str(v) for v in self.immediate_actions]

        if self.notification_required is not None and not isinstance(self.notification_required, Bool):
            self.notification_required = Bool(self.notification_required)

        if not isinstance(self.notifications_made, list):
            self.notifications_made = [self.notifications_made] if self.notifications_made is not None else []
        self.notifications_made = [v if isinstance(v, str) else str(v) for v in self.notifications_made]

        if not isinstance(self.remediation_actions, list):
            self.remediation_actions = [self.remediation_actions] if self.remediation_actions is not None else []
        self.remediation_actions = [v if isinstance(v, str) else str(v) for v in self.remediation_actions]

        if self.lessons_learned is not None and not isinstance(self.lessons_learned, str):
            self.lessons_learned = str(self.lessons_learned)

        if self.closure_datetime is not None and not isinstance(self.closure_datetime, XSDDateTime):
            self.closure_datetime = XSDDateTime(self.closure_datetime)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PIIProcessingActivity(NamedEntity):
    """
    Schema class documenting a PII processing operation: its purpose, legal basis, operation types performed,
    categories of PII involved, responsible actors, applied controls, retention period, and any cross-border transfer
    safeguards.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO29100["PIIProcessingActivity"]
    class_class_curie: ClassVar[str] = "iso29100:PIIProcessingActivity"
    class_name: ClassVar[str] = "PIIProcessingActivity"
    class_model_uri: ClassVar[URIRef] = ISO29100.PIIProcessingActivity

    id: Union[str, PIIProcessingActivityId] = None
    name: str = None
    processing_purpose: Optional[str] = None
    legal_basis: Optional[str] = None
    operations_performed: Optional[Union[Union[str, "PIIProcessingOperation"], list[Union[str, "PIIProcessingOperation"]]]] = empty_list()
    pii_categories_processed: Optional[Union[str, list[str]]] = empty_list()
    sensitivity_levels_involved: Optional[Union[Union[str, "PIISensitivityCategory"], list[Union[str, "PIISensitivityCategory"]]]] = empty_list()
    controller_ref: Optional[Union[str, PIIControllerId]] = None
    processor_ref: Optional[Union[str, PIIProcessorId]] = None
    data_flows: Optional[Union[Union[str, PIIFlowScenarioId], list[Union[str, PIIFlowScenarioId]]]] = empty_list()
    retention_period: Optional[str] = None
    privacy_controls_applied: Optional[Union[Union[str, PrivacyControlId], list[Union[str, PrivacyControlId]]]] = empty_list()
    cross_border_transfer: Optional[Union[bool, Bool]] = None
    transfer_safeguards: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PIIProcessingActivityId):
            self.id = PIIProcessingActivityId(self.id)

        if self.processing_purpose is not None and not isinstance(self.processing_purpose, str):
            self.processing_purpose = str(self.processing_purpose)

        if self.legal_basis is not None and not isinstance(self.legal_basis, str):
            self.legal_basis = str(self.legal_basis)

        if not isinstance(self.operations_performed, list):
            self.operations_performed = [self.operations_performed] if self.operations_performed is not None else []
        self.operations_performed = [v if isinstance(v, PIIProcessingOperation) else PIIProcessingOperation(v) for v in self.operations_performed]

        if not isinstance(self.pii_categories_processed, list):
            self.pii_categories_processed = [self.pii_categories_processed] if self.pii_categories_processed is not None else []
        self.pii_categories_processed = [v if isinstance(v, str) else str(v) for v in self.pii_categories_processed]

        if not isinstance(self.sensitivity_levels_involved, list):
            self.sensitivity_levels_involved = [self.sensitivity_levels_involved] if self.sensitivity_levels_involved is not None else []
        self.sensitivity_levels_involved = [v if isinstance(v, PIISensitivityCategory) else PIISensitivityCategory(v) for v in self.sensitivity_levels_involved]

        if self.controller_ref is not None and not isinstance(self.controller_ref, PIIControllerId):
            self.controller_ref = PIIControllerId(self.controller_ref)

        if self.processor_ref is not None and not isinstance(self.processor_ref, PIIProcessorId):
            self.processor_ref = PIIProcessorId(self.processor_ref)

        if not isinstance(self.data_flows, list):
            self.data_flows = [self.data_flows] if self.data_flows is not None else []
        self.data_flows = [v if isinstance(v, PIIFlowScenarioId) else PIIFlowScenarioId(v) for v in self.data_flows]

        if self.retention_period is not None and not isinstance(self.retention_period, str):
            self.retention_period = str(self.retention_period)

        if not isinstance(self.privacy_controls_applied, list):
            self.privacy_controls_applied = [self.privacy_controls_applied] if self.privacy_controls_applied is not None else []
        self.privacy_controls_applied = [v if isinstance(v, PrivacyControlId) else PrivacyControlId(v) for v in self.privacy_controls_applied]

        if self.cross_border_transfer is not None and not isinstance(self.cross_border_transfer, Bool):
            self.cross_border_transfer = Bool(self.cross_border_transfer)

        if not isinstance(self.transfer_safeguards, list):
            self.transfer_safeguards = [self.transfer_safeguards] if self.transfer_safeguards is not None else []
        self.transfer_safeguards = [v if isinstance(v, str) else str(v) for v in self.transfer_safeguards]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PrivacyPrincipleImplementation(NamedEntity):
    """
    Documentation of how a specific privacy principle from Clause 6 has been implemented within the organization's
    privacy framework, including measures taken and evidence of adherence.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO29100["PrivacyPrincipleImplementation"]
    class_class_curie: ClassVar[str] = "iso29100:PrivacyPrincipleImplementation"
    class_name: ClassVar[str] = "PrivacyPrincipleImplementation"
    class_model_uri: ClassVar[URIRef] = ISO29100.PrivacyPrincipleImplementation

    id: Union[str, PrivacyPrincipleImplementationId] = None
    name: str = None
    principle: Union[str, "PrivacyPrinciple"] = None
    implementation_measures: Optional[Union[str, list[str]]] = empty_list()
    applicable_controls_ref: Optional[Union[Union[str, PrivacyControlId], list[Union[str, PrivacyControlId]]]] = empty_list()
    evidence_of_adherence: Optional[Union[str, list[str]]] = empty_list()
    gaps_identified: Optional[Union[str, list[str]]] = empty_list()
    improvement_actions: Optional[Union[str, list[str]]] = empty_list()
    last_assessed_date: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PrivacyPrincipleImplementationId):
            self.id = PrivacyPrincipleImplementationId(self.id)

        if self._is_empty(self.principle):
            self.MissingRequiredField("principle")
        if not isinstance(self.principle, PrivacyPrinciple):
            self.principle = PrivacyPrinciple(self.principle)

        if not isinstance(self.implementation_measures, list):
            self.implementation_measures = [self.implementation_measures] if self.implementation_measures is not None else []
        self.implementation_measures = [v if isinstance(v, str) else str(v) for v in self.implementation_measures]

        if not isinstance(self.applicable_controls_ref, list):
            self.applicable_controls_ref = [self.applicable_controls_ref] if self.applicable_controls_ref is not None else []
        self.applicable_controls_ref = [v if isinstance(v, PrivacyControlId) else PrivacyControlId(v) for v in self.applicable_controls_ref]

        if not isinstance(self.evidence_of_adherence, list):
            self.evidence_of_adherence = [self.evidence_of_adherence] if self.evidence_of_adherence is not None else []
        self.evidence_of_adherence = [v if isinstance(v, str) else str(v) for v in self.evidence_of_adherence]

        if not isinstance(self.gaps_identified, list):
            self.gaps_identified = [self.gaps_identified] if self.gaps_identified is not None else []
        self.gaps_identified = [v if isinstance(v, str) else str(v) for v in self.gaps_identified]

        if not isinstance(self.improvement_actions, list):
            self.improvement_actions = [self.improvement_actions] if self.improvement_actions is not None else []
        self.improvement_actions = [v if isinstance(v, str) else str(v) for v in self.improvement_actions]

        if self.last_assessed_date is not None and not isinstance(self.last_assessed_date, XSDDate):
            self.last_assessed_date = XSDDate(self.last_assessed_date)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ConsentRecord(NamedEntity):
    """
    Schema class documenting a PII principal's agreement to processing of their PII for stated purposes. Records the
    consent mechanism used, scope, current status, and withdrawal date — supporting auditability of the consent and
    choice privacy principle.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO29100["ConsentRecord"]
    class_class_curie: ClassVar[str] = "iso29100:ConsentRecord"
    class_name: ClassVar[str] = "ConsentRecord"
    class_model_uri: ClassVar[URIRef] = ISO29100.ConsentRecord

    id: Union[str, ConsentRecordId] = None
    name: str = None
    principal_ref: Optional[str] = None
    consent_date: Optional[Union[str, XSDDateTime]] = None
    consent_mechanism: Optional[Union[str, "ConsentMechanism"]] = None
    processing_purposes_consented: Optional[Union[str, list[str]]] = empty_list()
    pii_categories_consented: Optional[Union[str, list[str]]] = empty_list()
    withdrawal_date: Optional[Union[str, XSDDateTime]] = None
    consent_status: Optional[str] = None
    consent_evidence_ref: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ConsentRecordId):
            self.id = ConsentRecordId(self.id)

        if self.principal_ref is not None and not isinstance(self.principal_ref, str):
            self.principal_ref = str(self.principal_ref)

        if self.consent_date is not None and not isinstance(self.consent_date, XSDDateTime):
            self.consent_date = XSDDateTime(self.consent_date)

        if self.consent_mechanism is not None and not isinstance(self.consent_mechanism, ConsentMechanism):
            self.consent_mechanism = ConsentMechanism(self.consent_mechanism)

        if not isinstance(self.processing_purposes_consented, list):
            self.processing_purposes_consented = [self.processing_purposes_consented] if self.processing_purposes_consented is not None else []
        self.processing_purposes_consented = [v if isinstance(v, str) else str(v) for v in self.processing_purposes_consented]

        if not isinstance(self.pii_categories_consented, list):
            self.pii_categories_consented = [self.pii_categories_consented] if self.pii_categories_consented is not None else []
        self.pii_categories_consented = [v if isinstance(v, str) else str(v) for v in self.pii_categories_consented]

        if self.withdrawal_date is not None and not isinstance(self.withdrawal_date, XSDDateTime):
            self.withdrawal_date = XSDDateTime(self.withdrawal_date)

        if self.consent_status is not None and not isinstance(self.consent_status, str):
            self.consent_status = str(self.consent_status)

        if self.consent_evidence_ref is not None and not isinstance(self.consent_evidence_ref, str):
            self.consent_evidence_ref = str(self.consent_evidence_ref)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PrivacyPreference(NamedEntity):
    """
    Schema class capturing a PII principal's processing choices for a particular purpose scope: preferences for
    anonymity or pseudonymity, restrictions on specific processing operations, and restrictions on disclosure to named
    or categorized parties.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ISO29100["PrivacyPreference"]
    class_class_curie: ClassVar[str] = "iso29100:PrivacyPreference"
    class_name: ClassVar[str] = "PrivacyPreference"
    class_model_uri: ClassVar[URIRef] = ISO29100.PrivacyPreference

    id: Union[str, PrivacyPreferenceId] = None
    name: str = None
    principal_ref: Optional[str] = None
    preference_scope: Optional[str] = None
    anonymity_preference: Optional[Union[bool, Bool]] = None
    pseudonymity_preference: Optional[Union[bool, Bool]] = None
    processing_restriction_preferences: Optional[Union[Union[str, "PIIProcessingOperation"], list[Union[str, "PIIProcessingOperation"]]]] = empty_list()
    disclosure_restriction_preferences: Optional[Union[str, list[str]]] = empty_list()
    preference_recorded_date: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PrivacyPreferenceId):
            self.id = PrivacyPreferenceId(self.id)

        if self.principal_ref is not None and not isinstance(self.principal_ref, str):
            self.principal_ref = str(self.principal_ref)

        if self.preference_scope is not None and not isinstance(self.preference_scope, str):
            self.preference_scope = str(self.preference_scope)

        if self.anonymity_preference is not None and not isinstance(self.anonymity_preference, Bool):
            self.anonymity_preference = Bool(self.anonymity_preference)

        if self.pseudonymity_preference is not None and not isinstance(self.pseudonymity_preference, Bool):
            self.pseudonymity_preference = Bool(self.pseudonymity_preference)

        if not isinstance(self.processing_restriction_preferences, list):
            self.processing_restriction_preferences = [self.processing_restriction_preferences] if self.processing_restriction_preferences is not None else []
        self.processing_restriction_preferences = [v if isinstance(v, PIIProcessingOperation) else PIIProcessingOperation(v) for v in self.processing_restriction_preferences]

        if not isinstance(self.disclosure_restriction_preferences, list):
            self.disclosure_restriction_preferences = [self.disclosure_restriction_preferences] if self.disclosure_restriction_preferences is not None else []
        self.disclosure_restriction_preferences = [v if isinstance(v, str) else str(v) for v in self.disclosure_restriction_preferences]

        if self.preference_recorded_date is not None and not isinstance(self.preference_recorded_date, XSDDate):
            self.preference_recorded_date = XSDDate(self.preference_recorded_date)

        super().__post_init__(**kwargs)


# Enumerations
class PrivacyPrinciple(EnumDefinitionImpl):
    """
    The eleven privacy principles defined in ISO/IEC 29100:2024 Clause 6 that govern the processing of PII in ICT
    systems.
    """
    consent_and_choice = PermissibleValue(
        text="consent_and_choice",
        description="""Schema value for privacy principle 1 (Clause 6.2): the organization gives PII principals meaningful choice over processing of their PII, manages opt-in consent mechanisms, and provides readily accessible means to withdraw consent.""",
        meaning=DPV["InformedConsent"])
    purpose_legitimacy_and_specification = PermissibleValue(
        text="purpose_legitimacy_and_specification",
        description="""Schema value for privacy principle 2 (Clause 6.3): the organization ensures each processing purpose is lawful, relies on a valid legal basis, and is communicated to PII principals prior to or at the time of collection.""",
        meaning=DPV["Purpose"])
    collection_limitation = PermissibleValue(
        text="collection_limitation",
        description="""Schema value for privacy principle 3 (Clause 6.4): the organization limits PII collection to what is lawful and strictly necessary to fulfil the stated processing purposes.""")
    data_minimization = PermissibleValue(
        text="data_minimization",
        description="""Schema value for privacy principle 4 (Clause 6.5): the organization designs processing procedures and ICT systems to minimize the volume of PII handled and the number of parties with access to it.""")
    use_retention_and_disclosure_limitation = PermissibleValue(
        text="use_retention_and_disclosure_limitation",
        description="""Schema value for privacy principle 5 (Clause 6.6): the organization limits use, retention, and disclosure of PII to the minimum needed for legitimate purposes, and securely disposes of PII once those purposes have been fulfilled.""")
    accuracy_and_quality = PermissibleValue(
        text="accuracy_and_quality",
        description="""Schema value for privacy principle 6 (Clause 6.7): the organization ensures PII is accurate, complete, current, and fit for purpose, and establishes procedures for verification, correction, and ongoing quality control of processed PII.""")
    openness_transparency_and_notice = PermissibleValue(
        text="openness_transparency_and_notice",
        description="""Schema value for privacy principle 7 (Clause 6.8): the organization provides PII principals with clear, accessible information about its PII processing policies and practices, and notifies them of material changes to those policies.""")
    individual_participation_and_access = PermissibleValue(
        text="individual_participation_and_access",
        description="""Schema value for privacy principle 8 (Clause 6.9): the organization gives PII principals the ability to access and review their PII and to challenge its accuracy and completeness, subject to applicable law.""",
        meaning=DPV["DataSubjectRight"])
    accountability = PermissibleValue(
        text="accountability",
        description="""Schema value for privacy principle 9 (Clause 6.10): the organization documents and communicates its privacy obligations, ensures equivalent protection when transferring PII to third parties, and maintains internal complaint-handling and redress procedures.""")
    information_security = PermissibleValue(
        text="information_security",
        description="""Schema value for privacy principle 10 (Clause 6.11): the organization applies appropriate security controls across operational, functional, and strategic levels to protect PII against unauthorized access, loss, or misuse throughout its full lifecycle.""")
    privacy_compliance = PermissibleValue(
        text="privacy_compliance",
        description="""Schema value for privacy principle 11 (Clause 6.12): the organization verifies and demonstrates compliance with data protection and privacy requirements through audits, independent internal controls, and ongoing privacy risk assessments.""",
        meaning=DPV["ComplianceAssessment"])

    _defn = EnumDefinition(
        name="PrivacyPrinciple",
        description="""The eleven privacy principles defined in ISO/IEC 29100:2024 Clause 6 that govern the processing of PII in ICT systems.""",
    )

class PIIFlowRole(EnumDefinitionImpl):
    """
    The role played by an actor in a specific PII flow scenario, as described in Table 1 of ISO/IEC 29100:2024 Clause
    5.3.
    """
    pii_provider = PermissibleValue(
        text="pii_provider",
        description="Actor that provides PII to another party in this flow scenario.")
    pii_recipient = PermissibleValue(
        text="pii_recipient",
        description="Actor that receives PII from another party in this flow scenario.")
    not_involved = PermissibleValue(
        text="not_involved",
        description="Actor not directly involved in this specific PII flow scenario.")

    _defn = EnumDefinition(
        name="PIIFlowRole",
        description="""The role played by an actor in a specific PII flow scenario, as described in Table 1 of ISO/IEC 29100:2024 Clause 5.3.""",
    )

class PIIProcessingOperation(EnumDefinitionImpl):
    """
    Categories of operations that can be performed on PII, as referenced in the definition of processing of PII
    (Clause 3.21).
    """
    collection = PermissibleValue(
        text="collection",
        description="Gathering or acquiring PII from PII principals or other sources.",
        meaning=DPV["Collect"])
    storage = PermissibleValue(
        text="storage",
        description="Storing PII in a persistent manner in ICT systems or other media.",
        meaning=DPV["Store"])
    alteration = PermissibleValue(
        text="alteration",
        description="Modifying or updating existing PII.",
        meaning=DPV["Transform"])
    retrieval = PermissibleValue(
        text="retrieval",
        description="Accessing or fetching stored PII for use.",
        meaning=DPV["Access"])
    consultation = PermissibleValue(
        text="consultation",
        description="Reviewing or examining PII without necessarily extracting it.",
        meaning=DPV["Use"])
    disclosure = PermissibleValue(
        text="disclosure",
        description="Making PII available to other parties or making it accessible.",
        meaning=DPV["Disclose"])
    anonymization = PermissibleValue(
        text="anonymization",
        description="""Irreversibly altering PII such that the PII principal can no longer be identified directly or indirectly.""",
        meaning=DPV["Anonymise"])
    pseudonymization = PermissibleValue(
        text="pseudonymization",
        description="""Replacing identifying information in PII with an alias, retaining linkability while restricting direct identification.""",
        meaning=DPV["Pseudonymise"])
    dissemination = PermissibleValue(
        text="dissemination",
        description="Widely distributing or publishing PII to multiple recipients.",
        meaning=DPV["Disseminate"])
    deletion = PermissibleValue(
        text="deletion",
        description="Removing PII such that it is no longer accessible or usable.",
        meaning=DPV["Erase"])
    destruction = PermissibleValue(
        text="destruction",
        description="Permanently and irrecoverably eliminating PII and its carriers.",
        meaning=DPV["Remove"])

    _defn = EnumDefinition(
        name="PIIProcessingOperation",
        description="""Categories of operations that can be performed on PII, as referenced in the definition of processing of PII (Clause 3.21).""",
    )

class SafeguardingRequirementFactor(EnumDefinitionImpl):
    """
    Categories of factors that influence an organization's privacy safeguarding requirements, as described in Clause
    5.5 and Figure 1.
    """
    legal_and_regulatory = PermissibleValue(
        text="legal_and_regulatory",
        description="""Safeguarding requirements arising from applicable laws (international, national, and local), regulations, judicial decisions, and negotiated labour or work-council agreements.""",
        meaning=DPV["LegalBasis"])
    contractual = PermissibleValue(
        text="contractual",
        description="""Safeguarding requirements set out in data processing agreements, company policies, and binding corporate rules agreed between PII controllers, processors, and other parties.""",
        meaning=DPV["Contract"])
    business = PermissibleValue(
        text="business",
        description="""Safeguarding requirements driven by the application's characteristics, industry guidelines, codes of conduct, or standards voluntarily adopted by the organization as part of its business model.""")
    other = PermissibleValue(
        text="other",
        description="""Safeguarding requirements arising from PII principal privacy preferences, internal control frameworks, or technical standards voluntarily adopted by the organization.""")

    _defn = EnumDefinition(
        name="SafeguardingRequirementFactor",
        description="""Categories of factors that influence an organization's privacy safeguarding requirements, as described in Clause 5.5 and Figure 1.""",
    )

class PIISensitivityCategory(EnumDefinitionImpl):
    """
    Categories of PII based on sensitivity, distinguishing standard PII from sensitive PII as defined in Clause 3.23.
    """
    standard = PermissibleValue(
        text="standard",
        description="""PII that does not meet the threshold for sensitive PII but still requires appropriate privacy protection measures.""")
    sensitive = PermissibleValue(
        text="sensitive",
        description="""PII warranting heightened protection due to its potential for significant adverse impact on the individual, or because applicable law classifies it as a special category. Typical examples include health, biometric, financial, racial, religious, political, and sexual orientation data. Processing may require opt-in consent or specific legal authorization.""",
        meaning=DPV["SpecialCategoryPersonalData"])

    _defn = EnumDefinition(
        name="PIISensitivityCategory",
        description="""Categories of PII based on sensitivity, distinguishing standard PII from sensitive PII as defined in Clause 3.23.""",
    )

class ConsentMechanism(EnumDefinitionImpl):
    """
    The mechanism by which a PII principal provides or withholds consent for PII processing, as referenced in Clauses
    3.6 and 6.2.
    """
    opt_in = PermissibleValue(
        text="opt_in",
        description="""The PII principal must take an explicit action to express prior consent for their PII to be processed for a particular purpose.""",
        meaning=DPV["ExplicitlyExpressedConsent"])
    opt_out = PermissibleValue(
        text="opt_out",
        description="""The PII principal must take a separate action to withhold or withdraw consent; processing is presumed permitted unless that action is taken.""",
        meaning=DPV["ImpliedConsent"])
    implied = PermissibleValue(
        text="implied",
        description="""Consent implied by some action of the PII principal, such as placing an order or using a service, where applicable law permits.""")

    _defn = EnumDefinition(
        name="ConsentMechanism",
        description="""The mechanism by which a PII principal provides or withholds consent for PII processing, as referenced in Clauses 3.6 and 6.2.""",
    )

class PrivacyRiskLevel(EnumDefinitionImpl):
    """
    Qualitative assessment of privacy risk level based on likelihood and potential adverse consequences for PII
    principals.
    """
    low = PermissibleValue(
        text="low",
        description="Limited potential adverse consequences for PII principals.")
    medium = PermissibleValue(
        text="medium",
        description="Moderate risk requiring management attention and planned controls.")
    high = PermissibleValue(
        text="high",
        description="Significant risk with potentially serious consequences for PII principals.")
    very_high = PermissibleValue(
        text="very_high",
        description="""Severe risk with potentially catastrophic or irreversible consequences for PII principals requiring immediate treatment.""")

    _defn = EnumDefinition(
        name="PrivacyRiskLevel",
        description="""Qualitative assessment of privacy risk level based on likelihood and potential adverse consequences for PII principals.""",
    )

class PrivacyControlType(EnumDefinitionImpl):
    """
    Categories of privacy controls that treat privacy risks by reducing their likelihood or consequences, as noted in
    Clause 3.12 Note 1.
    """
    organizational = PermissibleValue(
        text="organizational",
        description="""Policies, procedures, guidelines, management practices, or organizational structures used as privacy controls.""",
        meaning=DPV["OrganisationalMeasure"])
    physical = PermissibleValue(
        text="physical",
        description="Physical measures protecting PII and PII processing infrastructure.",
        meaning=DPV["PhysicalMeasure"])
    technical = PermissibleValue(
        text="technical",
        description="""ICT measures, products, or services that protect privacy, including privacy enhancing technologies (PETs).""",
        meaning=DPV["TechnicalMeasure"])
    legal_contractual = PermissibleValue(
        text="legal_contractual",
        description="""Legal contracts, binding corporate rules, or data processing agreements implementing privacy safeguards.""",
        meaning=DPV["LegalMeasure"])

    _defn = EnumDefinition(
        name="PrivacyControlType",
        description="""Categories of privacy controls that treat privacy risks by reducing their likelihood or consequences, as noted in Clause 3.12 Note 1.""",
    )

# Slots
class slots:
    pass

slots.id = Slot(uri=DCTERMS.identifier, name="id", curie=DCTERMS.curie('identifier'),
                   model_uri=ISO29100.id, domain=None, range=URIRef)

slots.name = Slot(uri=RDFS.label, name="name", curie=RDFS.curie('label'),
                   model_uri=ISO29100.name, domain=None, range=str)

slots.description = Slot(uri=DCTERMS.description, name="description", curie=DCTERMS.curie('description'),
                   model_uri=ISO29100.description, domain=None, range=Optional[str])

slots.created_date = Slot(uri=DCTERMS.created, name="created_date", curie=DCTERMS.curie('created'),
                   model_uri=ISO29100.created_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.modified_date = Slot(uri=DCTERMS.modified, name="modified_date", curie=DCTERMS.curie('modified'),
                   model_uri=ISO29100.modified_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.organization_name = Slot(uri=ISO29100.organization_name, name="organization_name", curie=ISO29100.curie('organization_name'),
                   model_uri=ISO29100.organization_name, domain=None, range=Optional[str])

slots.ict_system_description = Slot(uri=ISO29100.ict_system_description, name="ict_system_description", curie=ISO29100.curie('ict_system_description'),
                   model_uri=ISO29100.ict_system_description, domain=None, range=Optional[str])

slots.applicable_jurisdictions = Slot(uri=ISO29100.applicable_jurisdictions, name="applicable_jurisdictions", curie=ISO29100.curie('applicable_jurisdictions'),
                   model_uri=ISO29100.applicable_jurisdictions, domain=None, range=Optional[Union[str, list[str]]])

slots.pii_controllers = Slot(uri=ISO29100.pii_controllers, name="pii_controllers", curie=ISO29100.curie('pii_controllers'),
                   model_uri=ISO29100.pii_controllers, domain=None, range=Optional[Union[dict[Union[str, PIIControllerId], Union[dict, PIIController]], list[Union[dict, PIIController]]]])

slots.pii_processors = Slot(uri=ISO29100.pii_processors, name="pii_processors", curie=ISO29100.curie('pii_processors'),
                   model_uri=ISO29100.pii_processors, domain=None, range=Optional[Union[dict[Union[str, PIIProcessorId], Union[dict, PIIProcessor]], list[Union[dict, PIIProcessor]]]])

slots.third_parties = Slot(uri=ISO29100.third_parties, name="third_parties", curie=ISO29100.curie('third_parties'),
                   model_uri=ISO29100.third_parties, domain=None, range=Optional[Union[dict[Union[str, ThirdPartyId], Union[dict, ThirdParty]], list[Union[dict, ThirdParty]]]])

slots.pii_principals_description = Slot(uri=ISO29100.pii_principals_description, name="pii_principals_description", curie=ISO29100.curie('pii_principals_description'),
                   model_uri=ISO29100.pii_principals_description, domain=None, range=Optional[str])

slots.privacy_policy = Slot(uri=ISO29100.privacy_policy, name="privacy_policy", curie=ISO29100.curie('privacy_policy'),
                   model_uri=ISO29100.privacy_policy, domain=None, range=Optional[Union[str, PrivacyPolicyId]])

slots.privacy_controls = Slot(uri=ISO29100.privacy_controls, name="privacy_controls", curie=ISO29100.curie('privacy_controls'),
                   model_uri=ISO29100.privacy_controls, domain=None, range=Optional[Union[dict[Union[str, PrivacyControlId], Union[dict, PrivacyControl]], list[Union[dict, PrivacyControl]]]])

slots.safeguarding_requirements = Slot(uri=ISO29100.safeguarding_requirements, name="safeguarding_requirements", curie=ISO29100.curie('safeguarding_requirements'),
                   model_uri=ISO29100.safeguarding_requirements, domain=None, range=Optional[Union[dict[Union[str, PrivacySafeguardingRequirementId], Union[dict, PrivacySafeguardingRequirement]], list[Union[dict, PrivacySafeguardingRequirement]]]])

slots.privacy_risks = Slot(uri=ISO29100.privacy_risks, name="privacy_risks", curie=ISO29100.curie('privacy_risks'),
                   model_uri=ISO29100.privacy_risks, domain=None, range=Optional[Union[dict[Union[str, PrivacyRiskId], Union[dict, PrivacyRisk]], list[Union[dict, PrivacyRisk]]]])

slots.privacy_impact_assessments = Slot(uri=ISO29100.privacy_impact_assessments, name="privacy_impact_assessments", curie=ISO29100.curie('privacy_impact_assessments'),
                   model_uri=ISO29100.privacy_impact_assessments, domain=None, range=Optional[Union[dict[Union[str, PrivacyImpactAssessmentId], Union[dict, PrivacyImpactAssessment]], list[Union[dict, PrivacyImpactAssessment]]]])

slots.privacy_breaches = Slot(uri=ISO29100.privacy_breaches, name="privacy_breaches", curie=ISO29100.curie('privacy_breaches'),
                   model_uri=ISO29100.privacy_breaches, domain=None, range=Optional[Union[dict[Union[str, PrivacyBreachId], Union[dict, PrivacyBreach]], list[Union[dict, PrivacyBreach]]]])

slots.pii_processing_activities = Slot(uri=ISO29100.pii_processing_activities, name="pii_processing_activities", curie=ISO29100.curie('pii_processing_activities'),
                   model_uri=ISO29100.pii_processing_activities, domain=None, range=Optional[Union[dict[Union[str, PIIProcessingActivityId], Union[dict, PIIProcessingActivity]], list[Union[dict, PIIProcessingActivity]]]])

slots.principle_implementations = Slot(uri=ISO29100.principle_implementations, name="principle_implementations", curie=ISO29100.curie('principle_implementations'),
                   model_uri=ISO29100.principle_implementations, domain=None, range=Optional[Union[dict[Union[str, PrivacyPrincipleImplementationId], Union[dict, PrivacyPrincipleImplementation]], list[Union[dict, PrivacyPrincipleImplementation]]]])

slots.contact_information = Slot(uri=ISO29100.contact_information, name="contact_information", curie=ISO29100.curie('contact_information'),
                   model_uri=ISO29100.contact_information, domain=None, range=Optional[str])

slots.jurisdictions = Slot(uri=ISO29100.jurisdictions, name="jurisdictions", curie=ISO29100.curie('jurisdictions'),
                   model_uri=ISO29100.jurisdictions, domain=None, range=Optional[Union[str, list[str]]])

slots.privacy_preferences = Slot(uri=ISO29100.privacy_preferences, name="privacy_preferences", curie=ISO29100.curie('privacy_preferences'),
                   model_uri=ISO29100.privacy_preferences, domain=None, range=Optional[Union[dict[Union[str, PrivacyPreferenceId], Union[dict, PrivacyPreference]], list[Union[dict, PrivacyPreference]]]])

slots.consent_records = Slot(uri=ISO29100.consent_records, name="consent_records", curie=ISO29100.curie('consent_records'),
                   model_uri=ISO29100.consent_records, domain=None, range=Optional[Union[dict[Union[str, ConsentRecordId], Union[dict, ConsentRecord]], list[Union[dict, ConsentRecord]]]])

slots.processing_purposes = Slot(uri=ISO29100.processing_purposes, name="processing_purposes", curie=ISO29100.curie('processing_purposes'),
                   model_uri=ISO29100.processing_purposes, domain=None, range=Optional[Union[str, list[str]]])

slots.legal_bases = Slot(uri=ISO29100.legal_bases, name="legal_bases", curie=ISO29100.curie('legal_bases'),
                   model_uri=ISO29100.legal_bases, domain=None, range=Optional[Union[str, list[str]]])

slots.appointed_processors = Slot(uri=ISO29100.appointed_processors, name="appointed_processors", curie=ISO29100.curie('appointed_processors'),
                   model_uri=ISO29100.appointed_processors, domain=None, range=Optional[Union[Union[str, PIIProcessorId], list[Union[str, PIIProcessorId]]]])

slots.privacy_policy_ref = Slot(uri=ISO29100.privacy_policy_ref, name="privacy_policy_ref", curie=ISO29100.curie('privacy_policy_ref'),
                   model_uri=ISO29100.privacy_policy_ref, domain=None, range=Optional[Union[str, PrivacyPolicyId]])

slots.data_protection_officer = Slot(uri=ISO29100.data_protection_officer, name="data_protection_officer", curie=ISO29100.curie('data_protection_officer'),
                   model_uri=ISO29100.data_protection_officer, domain=None, range=Optional[str])

slots.instructing_controller = Slot(uri=ISO29100.instructing_controller, name="instructing_controller", curie=ISO29100.curie('instructing_controller'),
                   model_uri=ISO29100.instructing_controller, domain=None, range=Optional[Union[str, PIIControllerId]])

slots.processing_agreement_ref = Slot(uri=ISO29100.processing_agreement_ref, name="processing_agreement_ref", curie=ISO29100.curie('processing_agreement_ref'),
                   model_uri=ISO29100.processing_agreement_ref, domain=None, range=Optional[str])

slots.sub_processors = Slot(uri=ISO29100.sub_processors, name="sub_processors", curie=ISO29100.curie('sub_processors'),
                   model_uri=ISO29100.sub_processors, domain=None, range=Optional[Union[Union[str, PIIProcessorId], list[Union[str, PIIProcessorId]]]])

slots.receiving_purpose = Slot(uri=ISO29100.receiving_purpose, name="receiving_purpose", curie=ISO29100.curie('receiving_purpose'),
                   model_uri=ISO29100.receiving_purpose, domain=None, range=Optional[str])

slots.transfer_basis = Slot(uri=ISO29100.transfer_basis, name="transfer_basis", curie=ISO29100.curie('transfer_basis'),
                   model_uri=ISO29100.transfer_basis, domain=None, range=Optional[str])

slots.pii_category = Slot(uri=ISO29100.pii_category, name="pii_category", curie=ISO29100.curie('pii_category'),
                   model_uri=ISO29100.pii_category, domain=None, range=Optional[Union[str, list[str]]])

slots.sensitivity_level = Slot(uri=ISO29100.sensitivity_level, name="sensitivity_level", curie=ISO29100.curie('sensitivity_level'),
                   model_uri=ISO29100.sensitivity_level, domain=None, range=Optional[Union[str, "PIISensitivityCategory"]])

slots.identifier_type = Slot(uri=ISO29100.identifier_type, name="identifier_type", curie=ISO29100.curie('identifier_type'),
                   model_uri=ISO29100.identifier_type, domain=None, range=Optional[str])

slots.is_pseudonymized = Slot(uri=ISO29100.is_pseudonymized, name="is_pseudonymized", curie=ISO29100.curie('is_pseudonymized'),
                   model_uri=ISO29100.is_pseudonymized, domain=None, range=Optional[Union[bool, Bool]])

slots.is_anonymized = Slot(uri=ISO29100.is_anonymized, name="is_anonymized", curie=ISO29100.curie('is_anonymized'),
                   model_uri=ISO29100.is_anonymized, domain=None, range=Optional[Union[bool, Bool]])

slots.linkability_risk = Slot(uri=ISO29100.linkability_risk, name="linkability_risk", curie=ISO29100.curie('linkability_risk'),
                   model_uri=ISO29100.linkability_risk, domain=None, range=Optional[str])

slots.applicable_to_principal = Slot(uri=ISO29100.applicable_to_principal, name="applicable_to_principal", curie=ISO29100.curie('applicable_to_principal'),
                   model_uri=ISO29100.applicable_to_principal, domain=None, range=Optional[str])

slots.retention_schedule = Slot(uri=ISO29100.retention_schedule, name="retention_schedule", curie=ISO29100.curie('retention_schedule'),
                   model_uri=ISO29100.retention_schedule, domain=None, range=Optional[str])

slots.processing_operations = Slot(uri=ISO29100.processing_operations, name="processing_operations", curie=ISO29100.curie('processing_operations'),
                   model_uri=ISO29100.processing_operations, domain=None, range=Optional[Union[Union[str, "PIIProcessingOperation"], list[Union[str, "PIIProcessingOperation"]]]])

slots.scenario_label = Slot(uri=ISO29100.scenario_label, name="scenario_label", curie=ISO29100.curie('scenario_label'),
                   model_uri=ISO29100.scenario_label, domain=None, range=Optional[str])

slots.pii_principal_role = Slot(uri=ISO29100.pii_principal_role, name="pii_principal_role", curie=ISO29100.curie('pii_principal_role'),
                   model_uri=ISO29100.pii_principal_role, domain=None, range=Optional[Union[str, "PIIFlowRole"]])

slots.pii_controller_role = Slot(uri=ISO29100.pii_controller_role, name="pii_controller_role", curie=ISO29100.curie('pii_controller_role'),
                   model_uri=ISO29100.pii_controller_role, domain=None, range=Optional[Union[str, "PIIFlowRole"]])

slots.pii_processor_role = Slot(uri=ISO29100.pii_processor_role, name="pii_processor_role", curie=ISO29100.curie('pii_processor_role'),
                   model_uri=ISO29100.pii_processor_role, domain=None, range=Optional[Union[str, "PIIFlowRole"]])

slots.third_party_role = Slot(uri=ISO29100.third_party_role, name="third_party_role", curie=ISO29100.curie('third_party_role'),
                   model_uri=ISO29100.third_party_role, domain=None, range=Optional[Union[str, "PIIFlowRole"]])

slots.scenario_description = Slot(uri=ISO29100.scenario_description, name="scenario_description", curie=ISO29100.curie('scenario_description'),
                   model_uri=ISO29100.scenario_description, domain=None, range=Optional[str])

slots.legal_control_retention = Slot(uri=ISO29100.legal_control_retention, name="legal_control_retention", curie=ISO29100.curie('legal_control_retention'),
                   model_uri=ISO29100.legal_control_retention, domain=None, range=Optional[str])

slots.requirement_factor = Slot(uri=ISO29100.requirement_factor, name="requirement_factor", curie=ISO29100.curie('requirement_factor'),
                   model_uri=ISO29100.requirement_factor, domain=None, range=Optional[Union[str, "SafeguardingRequirementFactor"]])

slots.requirement_text = Slot(uri=ISO29100.requirement_text, name="requirement_text", curie=ISO29100.curie('requirement_text'),
                   model_uri=ISO29100.requirement_text, domain=None, range=Optional[str])

slots.source_reference = Slot(uri=ISO29100.source_reference, name="source_reference", curie=ISO29100.curie('source_reference'),
                   model_uri=ISO29100.source_reference, domain=None, range=Optional[str])

slots.applicable_to_actors = Slot(uri=ISO29100.applicable_to_actors, name="applicable_to_actors", curie=ISO29100.curie('applicable_to_actors'),
                   model_uri=ISO29100.applicable_to_actors, domain=None, range=Optional[Union[str, list[str]]])

slots.related_controls = Slot(uri=ISO29100.related_controls, name="related_controls", curie=ISO29100.curie('related_controls'),
                   model_uri=ISO29100.related_controls, domain=None, range=Optional[Union[Union[str, PrivacyControlId], list[Union[str, PrivacyControlId]]]])

slots.priority = Slot(uri=ISO29100.priority, name="priority", curie=ISO29100.curie('priority'),
                   model_uri=ISO29100.priority, domain=None, range=Optional[str])

slots.policy_version = Slot(uri=DCTERMS.hasVersion, name="policy_version", curie=DCTERMS.curie('hasVersion'),
                   model_uri=ISO29100.policy_version, domain=None, range=Optional[str])

slots.effective_date = Slot(uri=ISO29100.effective_date, name="effective_date", curie=ISO29100.curie('effective_date'),
                   model_uri=ISO29100.effective_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.policy_scope = Slot(uri=ISO29100.policy_scope, name="policy_scope", curie=ISO29100.curie('policy_scope'),
                   model_uri=ISO29100.policy_scope, domain=None, range=Optional[str])

slots.processing_purposes_covered = Slot(uri=ISO29100.processing_purposes_covered, name="processing_purposes_covered", curie=ISO29100.curie('processing_purposes_covered'),
                   model_uri=ISO29100.processing_purposes_covered, domain=None, range=Optional[Union[str, list[str]]])

slots.pii_categories_covered = Slot(uri=ISO29100.pii_categories_covered, name="pii_categories_covered", curie=ISO29100.curie('pii_categories_covered'),
                   model_uri=ISO29100.pii_categories_covered, domain=None, range=Optional[Union[str, list[str]]])

slots.data_retention_statement = Slot(uri=ISO29100.data_retention_statement, name="data_retention_statement", curie=ISO29100.curie('data_retention_statement'),
                   model_uri=ISO29100.data_retention_statement, domain=None, range=Optional[str])

slots.pii_principal_rights = Slot(uri=ISO29100.pii_principal_rights, name="pii_principal_rights", curie=ISO29100.curie('pii_principal_rights'),
                   model_uri=ISO29100.pii_principal_rights, domain=None, range=Optional[Union[str, list[str]]])

slots.contact_for_inquiries = Slot(uri=ISO29100.contact_for_inquiries, name="contact_for_inquiries", curie=ISO29100.curie('contact_for_inquiries'),
                   model_uri=ISO29100.contact_for_inquiries, domain=None, range=Optional[str])

slots.last_review_date = Slot(uri=ISO29100.last_review_date, name="last_review_date", curie=ISO29100.curie('last_review_date'),
                   model_uri=ISO29100.last_review_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.is_external_notice = Slot(uri=ISO29100.is_external_notice, name="is_external_notice", curie=ISO29100.curie('is_external_notice'),
                   model_uri=ISO29100.is_external_notice, domain=None, range=Optional[Union[bool, Bool]])

slots.applicable_principles = Slot(uri=ISO29100.applicable_principles, name="applicable_principles", curie=ISO29100.curie('applicable_principles'),
                   model_uri=ISO29100.applicable_principles, domain=None, range=Optional[Union[Union[str, "PrivacyPrinciple"], list[Union[str, "PrivacyPrinciple"]]]])

slots.control_type = Slot(uri=ISO29100.control_type, name="control_type", curie=ISO29100.curie('control_type'),
                   model_uri=ISO29100.control_type, domain=None, range=Optional[Union[str, "PrivacyControlType"]])

slots.control_objective = Slot(uri=ISO29100.control_objective, name="control_objective", curie=ISO29100.curie('control_objective'),
                   model_uri=ISO29100.control_objective, domain=None, range=Optional[str])

slots.addressed_principles = Slot(uri=ISO29100.addressed_principles, name="addressed_principles", curie=ISO29100.curie('addressed_principles'),
                   model_uri=ISO29100.addressed_principles, domain=None, range=Optional[Union[Union[str, "PrivacyPrinciple"], list[Union[str, "PrivacyPrinciple"]]]])

slots.implementation_description = Slot(uri=ISO29100.implementation_description, name="implementation_description", curie=ISO29100.curie('implementation_description'),
                   model_uri=ISO29100.implementation_description, domain=None, range=Optional[str])

slots.responsible_actor = Slot(uri=ISO29100.responsible_actor, name="responsible_actor", curie=ISO29100.curie('responsible_actor'),
                   model_uri=ISO29100.responsible_actor, domain=None, range=Optional[str])

slots.implementation_status = Slot(uri=ISO29100.implementation_status, name="implementation_status", curie=ISO29100.curie('implementation_status'),
                   model_uri=ISO29100.implementation_status, domain=None, range=Optional[str])

slots.effectiveness_evidence = Slot(uri=ISO29100.effectiveness_evidence, name="effectiveness_evidence", curie=ISO29100.curie('effectiveness_evidence'),
                   model_uri=ISO29100.effectiveness_evidence, domain=None, range=Optional[Union[str, list[str]]])

slots.related_safeguarding_requirements = Slot(uri=ISO29100.related_safeguarding_requirements, name="related_safeguarding_requirements", curie=ISO29100.curie('related_safeguarding_requirements'),
                   model_uri=ISO29100.related_safeguarding_requirements, domain=None, range=Optional[Union[Union[str, PrivacySafeguardingRequirementId], list[Union[str, PrivacySafeguardingRequirementId]]]])

slots.is_pet = Slot(uri=ISO29100.is_pet, name="is_pet", curie=ISO29100.curie('is_pet'),
                   model_uri=ISO29100.is_pet, domain=None, range=Optional[Union[bool, Bool]])

slots.risk_source = Slot(uri=ISO29100.risk_source, name="risk_source", curie=ISO29100.curie('risk_source'),
                   model_uri=ISO29100.risk_source, domain=None, range=Optional[str])

slots.affected_pii_categories = Slot(uri=ISO29100.affected_pii_categories, name="affected_pii_categories", curie=ISO29100.curie('affected_pii_categories'),
                   model_uri=ISO29100.affected_pii_categories, domain=None, range=Optional[Union[str, list[str]]])

slots.affected_principals_description = Slot(uri=ISO29100.affected_principals_description, name="affected_principals_description", curie=ISO29100.curie('affected_principals_description'),
                   model_uri=ISO29100.affected_principals_description, domain=None, range=Optional[str])

slots.risk_likelihood = Slot(uri=ISO29100.risk_likelihood, name="risk_likelihood", curie=ISO29100.curie('risk_likelihood'),
                   model_uri=ISO29100.risk_likelihood, domain=None, range=Optional[str])

slots.risk_impact_description = Slot(uri=ISO29100.risk_impact_description, name="risk_impact_description", curie=ISO29100.curie('risk_impact_description'),
                   model_uri=ISO29100.risk_impact_description, domain=None, range=Optional[str])

slots.inherent_risk_level = Slot(uri=ISO29100.inherent_risk_level, name="inherent_risk_level", curie=ISO29100.curie('inherent_risk_level'),
                   model_uri=ISO29100.inherent_risk_level, domain=None, range=Optional[Union[str, "PrivacyRiskLevel"]])

slots.residual_risk_level = Slot(uri=ISO29100.residual_risk_level, name="residual_risk_level", curie=ISO29100.curie('residual_risk_level'),
                   model_uri=ISO29100.residual_risk_level, domain=None, range=Optional[Union[str, "PrivacyRiskLevel"]])

slots.mitigating_controls = Slot(uri=ISO29100.mitigating_controls, name="mitigating_controls", curie=ISO29100.curie('mitigating_controls'),
                   model_uri=ISO29100.mitigating_controls, domain=None, range=Optional[Union[Union[str, PrivacyControlId], list[Union[str, PrivacyControlId]]]])

slots.risk_owner = Slot(uri=ISO29100.risk_owner, name="risk_owner", curie=ISO29100.curie('risk_owner'),
                   model_uri=ISO29100.risk_owner, domain=None, range=Optional[str])

slots.assessment_scope = Slot(uri=ISO29100.assessment_scope, name="assessment_scope", curie=ISO29100.curie('assessment_scope'),
                   model_uri=ISO29100.assessment_scope, domain=None, range=Optional[str])

slots.assessment_date = Slot(uri=ISO29100.assessment_date, name="assessment_date", curie=ISO29100.curie('assessment_date'),
                   model_uri=ISO29100.assessment_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.assessor = Slot(uri=ISO29100.assessor, name="assessor", curie=ISO29100.curie('assessor'),
                   model_uri=ISO29100.assessor, domain=None, range=Optional[str])

slots.processing_activities_assessed = Slot(uri=ISO29100.processing_activities_assessed, name="processing_activities_assessed", curie=ISO29100.curie('processing_activities_assessed'),
                   model_uri=ISO29100.processing_activities_assessed, domain=None, range=Optional[Union[Union[str, PIIProcessingActivityId], list[Union[str, PIIProcessingActivityId]]]])

slots.risks_identified = Slot(uri=ISO29100.risks_identified, name="risks_identified", curie=ISO29100.curie('risks_identified'),
                   model_uri=ISO29100.risks_identified, domain=None, range=Optional[Union[Union[str, PrivacyRiskId], list[Union[str, PrivacyRiskId]]]])

slots.risks_treated = Slot(uri=ISO29100.risks_treated, name="risks_treated", curie=ISO29100.curie('risks_treated'),
                   model_uri=ISO29100.risks_treated, domain=None, range=Optional[Union[Union[str, PrivacyRiskId], list[Union[str, PrivacyRiskId]]]])

slots.residual_risks_accepted = Slot(uri=ISO29100.residual_risks_accepted, name="residual_risks_accepted", curie=ISO29100.curie('residual_risks_accepted'),
                   model_uri=ISO29100.residual_risks_accepted, domain=None, range=Optional[Union[Union[str, PrivacyRiskId], list[Union[str, PrivacyRiskId]]]])

slots.assessment_outcome = Slot(uri=ISO29100.assessment_outcome, name="assessment_outcome", curie=ISO29100.curie('assessment_outcome'),
                   model_uri=ISO29100.assessment_outcome, domain=None, range=Optional[str])

slots.next_assessment_date = Slot(uri=ISO29100.next_assessment_date, name="next_assessment_date", curie=ISO29100.curie('next_assessment_date'),
                   model_uri=ISO29100.next_assessment_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.consultation_records = Slot(uri=ISO29100.consultation_records, name="consultation_records", curie=ISO29100.curie('consultation_records'),
                   model_uri=ISO29100.consultation_records, domain=None, range=Optional[Union[str, list[str]]])

slots.breach_datetime = Slot(uri=ISO29100.breach_datetime, name="breach_datetime", curie=ISO29100.curie('breach_datetime'),
                   model_uri=ISO29100.breach_datetime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.discovery_datetime = Slot(uri=ISO29100.discovery_datetime, name="discovery_datetime", curie=ISO29100.curie('discovery_datetime'),
                   model_uri=ISO29100.discovery_datetime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.breach_description = Slot(uri=ISO29100.breach_description, name="breach_description", curie=ISO29100.curie('breach_description'),
                   model_uri=ISO29100.breach_description, domain=None, range=Optional[str])

slots.affected_principals_count = Slot(uri=ISO29100.affected_principals_count, name="affected_principals_count", curie=ISO29100.curie('affected_principals_count'),
                   model_uri=ISO29100.affected_principals_count, domain=None, range=Optional[int])

slots.violated_requirements = Slot(uri=ISO29100.violated_requirements, name="violated_requirements", curie=ISO29100.curie('violated_requirements'),
                   model_uri=ISO29100.violated_requirements, domain=None, range=Optional[Union[Union[str, PrivacySafeguardingRequirementId], list[Union[str, PrivacySafeguardingRequirementId]]]])

slots.breach_severity = Slot(uri=ISO29100.breach_severity, name="breach_severity", curie=ISO29100.curie('breach_severity'),
                   model_uri=ISO29100.breach_severity, domain=None, range=Optional[Union[str, "PrivacyRiskLevel"]])

slots.immediate_actions = Slot(uri=ISO29100.immediate_actions, name="immediate_actions", curie=ISO29100.curie('immediate_actions'),
                   model_uri=ISO29100.immediate_actions, domain=None, range=Optional[Union[str, list[str]]])

slots.notification_required = Slot(uri=ISO29100.notification_required, name="notification_required", curie=ISO29100.curie('notification_required'),
                   model_uri=ISO29100.notification_required, domain=None, range=Optional[Union[bool, Bool]])

slots.notifications_made = Slot(uri=ISO29100.notifications_made, name="notifications_made", curie=ISO29100.curie('notifications_made'),
                   model_uri=ISO29100.notifications_made, domain=None, range=Optional[Union[str, list[str]]])

slots.remediation_actions = Slot(uri=ISO29100.remediation_actions, name="remediation_actions", curie=ISO29100.curie('remediation_actions'),
                   model_uri=ISO29100.remediation_actions, domain=None, range=Optional[Union[str, list[str]]])

slots.lessons_learned = Slot(uri=ISO29100.lessons_learned, name="lessons_learned", curie=ISO29100.curie('lessons_learned'),
                   model_uri=ISO29100.lessons_learned, domain=None, range=Optional[str])

slots.closure_datetime = Slot(uri=ISO29100.closure_datetime, name="closure_datetime", curie=ISO29100.curie('closure_datetime'),
                   model_uri=ISO29100.closure_datetime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.processing_purpose = Slot(uri=ISO29100.processing_purpose, name="processing_purpose", curie=ISO29100.curie('processing_purpose'),
                   model_uri=ISO29100.processing_purpose, domain=None, range=Optional[str])

slots.legal_basis = Slot(uri=ISO29100.legal_basis, name="legal_basis", curie=ISO29100.curie('legal_basis'),
                   model_uri=ISO29100.legal_basis, domain=None, range=Optional[str])

slots.operations_performed = Slot(uri=ISO29100.operations_performed, name="operations_performed", curie=ISO29100.curie('operations_performed'),
                   model_uri=ISO29100.operations_performed, domain=None, range=Optional[Union[Union[str, "PIIProcessingOperation"], list[Union[str, "PIIProcessingOperation"]]]])

slots.pii_categories_processed = Slot(uri=ISO29100.pii_categories_processed, name="pii_categories_processed", curie=ISO29100.curie('pii_categories_processed'),
                   model_uri=ISO29100.pii_categories_processed, domain=None, range=Optional[Union[str, list[str]]])

slots.sensitivity_levels_involved = Slot(uri=ISO29100.sensitivity_levels_involved, name="sensitivity_levels_involved", curie=ISO29100.curie('sensitivity_levels_involved'),
                   model_uri=ISO29100.sensitivity_levels_involved, domain=None, range=Optional[Union[Union[str, "PIISensitivityCategory"], list[Union[str, "PIISensitivityCategory"]]]])

slots.controller_ref = Slot(uri=ISO29100.controller_ref, name="controller_ref", curie=ISO29100.curie('controller_ref'),
                   model_uri=ISO29100.controller_ref, domain=None, range=Optional[Union[str, PIIControllerId]])

slots.processor_ref = Slot(uri=ISO29100.processor_ref, name="processor_ref", curie=ISO29100.curie('processor_ref'),
                   model_uri=ISO29100.processor_ref, domain=None, range=Optional[Union[str, PIIProcessorId]])

slots.data_flows = Slot(uri=ISO29100.data_flows, name="data_flows", curie=ISO29100.curie('data_flows'),
                   model_uri=ISO29100.data_flows, domain=None, range=Optional[Union[Union[str, PIIFlowScenarioId], list[Union[str, PIIFlowScenarioId]]]])

slots.retention_period = Slot(uri=ISO29100.retention_period, name="retention_period", curie=ISO29100.curie('retention_period'),
                   model_uri=ISO29100.retention_period, domain=None, range=Optional[str])

slots.privacy_controls_applied = Slot(uri=ISO29100.privacy_controls_applied, name="privacy_controls_applied", curie=ISO29100.curie('privacy_controls_applied'),
                   model_uri=ISO29100.privacy_controls_applied, domain=None, range=Optional[Union[Union[str, PrivacyControlId], list[Union[str, PrivacyControlId]]]])

slots.cross_border_transfer = Slot(uri=ISO29100.cross_border_transfer, name="cross_border_transfer", curie=ISO29100.curie('cross_border_transfer'),
                   model_uri=ISO29100.cross_border_transfer, domain=None, range=Optional[Union[bool, Bool]])

slots.transfer_safeguards = Slot(uri=ISO29100.transfer_safeguards, name="transfer_safeguards", curie=ISO29100.curie('transfer_safeguards'),
                   model_uri=ISO29100.transfer_safeguards, domain=None, range=Optional[Union[str, list[str]]])

slots.principle = Slot(uri=ISO29100.principle, name="principle", curie=ISO29100.curie('principle'),
                   model_uri=ISO29100.principle, domain=None, range=Union[str, "PrivacyPrinciple"])

slots.implementation_measures = Slot(uri=ISO29100.implementation_measures, name="implementation_measures", curie=ISO29100.curie('implementation_measures'),
                   model_uri=ISO29100.implementation_measures, domain=None, range=Optional[Union[str, list[str]]])

slots.applicable_controls_ref = Slot(uri=ISO29100.applicable_controls_ref, name="applicable_controls_ref", curie=ISO29100.curie('applicable_controls_ref'),
                   model_uri=ISO29100.applicable_controls_ref, domain=None, range=Optional[Union[Union[str, PrivacyControlId], list[Union[str, PrivacyControlId]]]])

slots.evidence_of_adherence = Slot(uri=ISO29100.evidence_of_adherence, name="evidence_of_adherence", curie=ISO29100.curie('evidence_of_adherence'),
                   model_uri=ISO29100.evidence_of_adherence, domain=None, range=Optional[Union[str, list[str]]])

slots.gaps_identified = Slot(uri=ISO29100.gaps_identified, name="gaps_identified", curie=ISO29100.curie('gaps_identified'),
                   model_uri=ISO29100.gaps_identified, domain=None, range=Optional[Union[str, list[str]]])

slots.improvement_actions = Slot(uri=ISO29100.improvement_actions, name="improvement_actions", curie=ISO29100.curie('improvement_actions'),
                   model_uri=ISO29100.improvement_actions, domain=None, range=Optional[Union[str, list[str]]])

slots.last_assessed_date = Slot(uri=ISO29100.last_assessed_date, name="last_assessed_date", curie=ISO29100.curie('last_assessed_date'),
                   model_uri=ISO29100.last_assessed_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.principal_ref = Slot(uri=ISO29100.principal_ref, name="principal_ref", curie=ISO29100.curie('principal_ref'),
                   model_uri=ISO29100.principal_ref, domain=None, range=Optional[str])

slots.consent_date = Slot(uri=ISO29100.consent_date, name="consent_date", curie=ISO29100.curie('consent_date'),
                   model_uri=ISO29100.consent_date, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.consent_mechanism = Slot(uri=ISO29100.consent_mechanism, name="consent_mechanism", curie=ISO29100.curie('consent_mechanism'),
                   model_uri=ISO29100.consent_mechanism, domain=None, range=Optional[Union[str, "ConsentMechanism"]])

slots.processing_purposes_consented = Slot(uri=ISO29100.processing_purposes_consented, name="processing_purposes_consented", curie=ISO29100.curie('processing_purposes_consented'),
                   model_uri=ISO29100.processing_purposes_consented, domain=None, range=Optional[Union[str, list[str]]])

slots.pii_categories_consented = Slot(uri=ISO29100.pii_categories_consented, name="pii_categories_consented", curie=ISO29100.curie('pii_categories_consented'),
                   model_uri=ISO29100.pii_categories_consented, domain=None, range=Optional[Union[str, list[str]]])

slots.withdrawal_date = Slot(uri=ISO29100.withdrawal_date, name="withdrawal_date", curie=ISO29100.curie('withdrawal_date'),
                   model_uri=ISO29100.withdrawal_date, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.consent_status = Slot(uri=ISO29100.consent_status, name="consent_status", curie=ISO29100.curie('consent_status'),
                   model_uri=ISO29100.consent_status, domain=None, range=Optional[str])

slots.consent_evidence_ref = Slot(uri=ISO29100.consent_evidence_ref, name="consent_evidence_ref", curie=ISO29100.curie('consent_evidence_ref'),
                   model_uri=ISO29100.consent_evidence_ref, domain=None, range=Optional[str])

slots.preference_scope = Slot(uri=ISO29100.preference_scope, name="preference_scope", curie=ISO29100.curie('preference_scope'),
                   model_uri=ISO29100.preference_scope, domain=None, range=Optional[str])

slots.anonymity_preference = Slot(uri=ISO29100.anonymity_preference, name="anonymity_preference", curie=ISO29100.curie('anonymity_preference'),
                   model_uri=ISO29100.anonymity_preference, domain=None, range=Optional[Union[bool, Bool]])

slots.pseudonymity_preference = Slot(uri=ISO29100.pseudonymity_preference, name="pseudonymity_preference", curie=ISO29100.curie('pseudonymity_preference'),
                   model_uri=ISO29100.pseudonymity_preference, domain=None, range=Optional[Union[bool, Bool]])

slots.processing_restriction_preferences = Slot(uri=ISO29100.processing_restriction_preferences, name="processing_restriction_preferences", curie=ISO29100.curie('processing_restriction_preferences'),
                   model_uri=ISO29100.processing_restriction_preferences, domain=None, range=Optional[Union[Union[str, "PIIProcessingOperation"], list[Union[str, "PIIProcessingOperation"]]]])

slots.disclosure_restriction_preferences = Slot(uri=ISO29100.disclosure_restriction_preferences, name="disclosure_restriction_preferences", curie=ISO29100.curie('disclosure_restriction_preferences'),
                   model_uri=ISO29100.disclosure_restriction_preferences, domain=None, range=Optional[Union[str, list[str]]])

slots.preference_recorded_date = Slot(uri=ISO29100.preference_recorded_date, name="preference_recorded_date", curie=ISO29100.curie('preference_recorded_date'),
                   model_uri=ISO29100.preference_recorded_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.NamedEntity_id = Slot(uri=DCTERMS.identifier, name="NamedEntity_id", curie=DCTERMS.curie('identifier'),
                   model_uri=ISO29100.NamedEntity_id, domain=NamedEntity, range=Union[str, NamedEntityId])
