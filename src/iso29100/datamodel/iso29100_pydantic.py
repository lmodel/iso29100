from __future__ import annotations

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal
from enum import Enum
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer
)


metamodel_version = "1.12.0"
version = "2024"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias = True,
        validate_by_name = True,
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )





class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'annotations': {'edition': {'tag': 'edition', 'value': '2'},
                     'iso_open_data_date': {'tag': 'iso_open_data_date',
                                            'value': '2026-11-05'},
                     'publication_date': {'tag': 'publication_date',
                                          'value': '2024-02-16'},
                     'replaces': {'tag': 'replaces',
                                  'value': 'ISO/IEC 29100:2011, ISO/IEC '
                                           '29100:2011/Amd 1:2018'},
                     'standard': {'tag': 'standard',
                                  'value': 'ISO/IEC 29100:2024'}},
     'comments': ['The version is the edition the schema models, and source is '
                  "ISO's page for it. ISO Open Data's records of the edition and "
                  'of the two it replaced are copied to '
                  'src/iso29100/schema/iso-open-data/ on the date the annotations '
                  'give, and scripts/check_upstream_release.py reports when ISO '
                  "changes them. The release tags are the schema's own versions.",
                  'ISO/IEC 29100 is copyright ISO and IEC, and none of its text is '
                  "reproduced here. An element's title and description are this "
                  "project's own words. An element cites what it models by number "
                  "in the iso29100_clause annotation only where a third party's "
                  'public outline of the edition gives that number, so terms and '
                  'lower subclauses go uncited. A reader with a licensed copy '
                  'looks the text up there.',
                  'Every record that other records refer to has a pf_id, and a '
                  'reference holds that identifier. PfFramework holds each kind of '
                  'record in a list of its own.',
                  'The mappings to the Data Privacy Vocabulary (DPV) are the five '
                  'rows DPV publishes for this edition, in upstream/dpv-iso.ttl, '
                  "with DPV's direction kept. No other mapping is declared, "
                  'because no source states one.'],
     'default_prefix': 'iso29100',
     'default_range': 'string',
     'description': 'A LinkML model of the records an organization keeps when it '
                    'applies the privacy framework of ISO/IEC 29100:2024 to the '
                    'information and communication technology (ICT) systems that '
                    'handle personally identifiable information (PII). The records '
                    'say who takes part, which PII is involved and how it moves, '
                    'what must be safeguarded and how, and how the organization '
                    'stands against each privacy principle.',
     'id': 'https://w3id.org/lmodel/iso29100',
     'imports': ['linkml:types'],
     'license': 'Apache-2.0',
     'name': 'iso29100',
     'prefixes': {'dpv': {'prefix_prefix': 'dpv',
                          'prefix_reference': 'https://w3id.org/dpv#'},
                  'iso29100': {'prefix_prefix': 'iso29100',
                               'prefix_reference': 'https://w3id.org/lmodel/iso29100/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'},
                  'xsd': {'prefix_prefix': 'xsd',
                          'prefix_reference': 'http://www.w3.org/2001/XMLSchema#'}},
     'see_also': ['https://lmodel.github.io/iso29100',
                  'https://www.iso.org/standard/85938.html'],
     'source': 'https://www.iso.org/standard/85938.html',
     'source_file': 'src/iso29100/schema/iso29100.yaml',
     'title': 'ISO/IEC 29100:2024 privacy framework records',
     'types': {'pf_duration': {'base': 'str',
                               'description': 'A length of time as ISO 8601 writes '
                                              'it, such as P7Y for seven years or '
                                              'P30D for thirty days.',
                               'from_schema': 'https://w3id.org/lmodel/iso29100',
                               'name': 'pf_duration',
                               'pattern': '^P(?=[0-9T])([0-9]+Y)?([0-9]+M)?([0-9]+W)?([0-9]+D)?(T(?=[0-9])([0-9]+H)?([0-9]+M)?([0-9]+S)?)?$',
                               'typeof': 'string',
                               'uri': 'xsd:duration'}}} )

class PfPrinciple(str, Enum):
    """
    The privacy principles by their subclause numbers. A value's title and description are this project's own summary, and the principles' headings and wording are ISO's.
    """
    number_6FULL_STOP2_People_decide = "principle_6_2"
    """
    People get a say in whether their PII is processed, can agree or refuse purpose by purpose, and can change their minds later.
    """
    number_6FULL_STOP3_Lawful_stated_reasons = "principle_6_3"
    """
    The law allows each reason for processing, and people are told the reason before their PII is gathered, or at that moment.
    """
    number_6FULL_STOP4_Gather_within_bounds = "principle_6_4"
    """
    The organization gathers only the PII that the law allows and its stated reasons need.
    """
    number_6FULL_STOP5_A_small_footprint = "principle_6_5"
    """
    Systems and procedures are built to touch as little PII as they can, and as few people as possible can reach it.
    """
    number_6FULL_STOP6_Bounded_use_and_keeping = "principle_6_6"
    """
    PII is used, shared and kept only as far as the stated reasons go, and is safely disposed of afterwards.
    """
    number_6FULL_STOP7_Correct_and_fit = "principle_6_7"
    """
    PII stays right, whole, up to date and suited to its use, and there are ways to check and fix it.
    """
    number_6FULL_STOP8_Say_what_happens = "principle_6_8"
    """
    People can easily find out what the organization does with PII, and hear about important changes.
    """
    number_6FULL_STOP9_People_see_their_own = "principle_6_9"
    """
    People can look at the PII held about them and dispute it, within what the law allows.
    """
    number_6FULL_STOP10_Answer_for_it = "principle_6_10"
    """
    The organization writes down its duties, keeps protection in place when PII passes to others, and handles complaints and redress.
    """
    number_6FULL_STOP11_Keep_it_safe = "principle_6_11"
    """
    Security measures at every level guard PII against loss and unauthorized reach for as long as it is held.
    """
    number_6FULL_STOP12_Show_the_rules_are_met = "principle_6_12"
    """
    The organization checks, and can prove, that it meets its privacy duties, through audits and regular risk assessment.
    """


class PfOperation(str, Enum):
    """
    The things an organization can do to PII.
    """
    collect = "collect"
    """
    Get PII from the person it is about, or from another source.
    """
    store = "store"
    """
    Hold PII on a lasting medium.
    """
    retrieve = "retrieve"
    """
    Fetch stored PII for use.
    """
    consult = "consult"
    """
    Look at PII without taking a copy away.
    """
    alter = "alter"
    """
    Change PII that is already held.
    """
    pseudonymize = "pseudonymize"
    """
    Swap identifying details for an alias, in a way someone can still trace back.
    """
    anonymize = "anonymize"
    """
    Change PII so that nobody can trace it back to a person again.
    """
    disclose = "disclose"
    """
    Make PII available to another party.
    """
    disseminate = "disseminate"
    """
    Spread PII widely, such as by publishing it.
    """
    delete = "delete"
    """
    Remove PII so that it can no longer be reached or used.
    """
    destroy = "destroy"
    """
    Remove PII and whatever carried it, beyond recovery.
    """


class PfPiiRecognition(str, Enum):
    """
    The ways information turns out to be PII, which a record lists so that a reader can see why the item counts.
    """
    direct_identifier = "direct_identifier"
    """
    It singles out one person by itself, such as a passport number.
    """
    distinguishing_trait = "distinguishing_trait"
    """
    It sets one person apart, alone or with other details, such as a rare job title in a small town.
    """
    linked_information = "linked_information"
    """
    It says something about a person who is already known, or can be joined to a record that does.
    """
    pseudonym = "pseudonym"
    """
    It holds an alias in place of an identifier, and the alias can be traced.
    """
    metadata = "metadata"
    """
    It describes other data, such as a message's sender and time, and so reveals a person.
    """
    unsolicited = "unsolicited"
    """
    The organization received it without asking for it.
    """


class PfSensitivity(str, Enum):
    """
    How much harm the PII could do to the person it is about.
    """
    ordinary = "ordinary"
    """
    It needs the usual protection for PII.
    """
    sensitive = "sensitive"
    """
    Its misuse could badly harm the person, or a law sets it apart, such as health data, so it needs stronger protection.
    """


class PfRequirementFactor(str, Enum):
    """
    Where a requirement to safeguard PII comes from.
    """
    law = "law"
    """
    A statute, a regulation, a court's ruling or a collective agreement.
    """
    contract = "contract"
    """
    An agreement between parties, such as one with a processor, or rules that bind a group of companies.
    """
    business = "business"
    """
    How the business or its application works, or a code of practice it chose to follow.
    """
    other = "other"
    """
    Another source, such as what people have said they prefer, or a technical standard the organization adopted.
    """


class PfPolicyAudience(str, Enum):
    """
    Who a privacy policy is written for.
    """
    internal = "internal"
    """
    People inside the organization, who act on its commitments.
    """
    public_notice = "public_notice"
    """
    The people whose PII it handles, who read it to learn what happens.
    """


class PfControlKind(str, Enum):
    """
    The form a control takes.
    """
    organizational = "organizational"
    """
    A policy, a procedure, a role or another way of running things.
    """
    physical = "physical"
    """
    A measure that guards the places and equipment where PII sits.
    """
    technical = "technical"
    """
    A system, product or service that protects PII.
    """
    privacy_enhancing_technology = "privacy_enhancing_technology"
    """
    A technical measure built to reduce what is collected or revealed about people.
    """
    contractual = "contractual"
    """
    A binding agreement, such as one with a processor or across a group of companies.
    """


class PfImplementationState(str, Enum):
    """
    How far a control has been put into effect.
    """
    planned = "planned"
    """
    It is decided on but not started.
    """
    in_progress = "in_progress"
    """
    It is being put in place.
    """
    in_operation = "in_operation"
    """
    It is in place and working.
    """
    retired = "retired"
    """
    It is no longer in use.
    """


class PfRiskLevel(str, Enum):
    """
    A qualitative level of risk to people, offered for an organization that adopts it, since the framework leaves the scale to the organization.
    """
    low = "low"
    """
    The harm to people would be limited.
    """
    medium = "medium"
    """
    The harm would call for planned measures.
    """
    high = "high"
    """
    The harm could be serious.
    """
    very_high = "very_high"
    """
    The harm could be severe or lasting, and needs treating at once.
    """


class PfConsentMechanism(str, Enum):
    """
    How a person's agreement to processing is obtained.
    """
    opt_in = "opt_in"
    """
    The person acts to agree before the processing starts.
    """
    opt_out = "opt_out"
    """
    The processing goes ahead unless the person acts to refuse it.
    """
    implied = "implied"
    """
    Something the person does shows agreement, such as placing an order, where the law allows that reading.
    """


class PfConsentState(str, Enum):
    """
    Where a person's agreement stands.
    """
    given = "given"
    """
    The agreement holds.
    """
    refused = "refused"
    """
    The person said no.
    """
    withdrawn = "withdrawn"
    """
    The person took back an agreement they had given.
    """
    expired = "expired"
    """
    The agreement ran out.
    """



class PfRecordMixin(ConfiguredBaseModel):
    """
    What every record of the framework has, so that other records can refer to it: an identifier, a title and a description.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['It is a mixin, not a base class, so that the adapt copy can '
                      "re-root some record classes on LOKF's Concept and leave the "
                      "others as they are. lokf adapt replaces pf_id with LOKF's id, "
                      'and a class that declares id itself must descend from Concept.'],
         'from_schema': 'https://w3id.org/lmodel/iso29100',
         'mixin': True,
         'slot_usage': {'title': {'name': 'title',
                                  'pattern': '^\\s*\\S',
                                  'required': True}}})

    pf_id: str = Field(default=..., description="""The record's identifier, unique among the records of the framework, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['PfRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['PfRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('pf_id')
    def pattern_pf_id(cls, v):
        pattern=re.compile(r"^\S+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid pf_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid pf_id format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class PfFramework(PfRecordMixin):
    """
    One organization's use of the privacy framework: the systems it covers, and every record the organization keeps about them, each kind in a list of its own.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso29100_clause': {'tag': 'iso29100_clause', 'value': '5.1'}},
         'from_schema': 'https://w3id.org/lmodel/iso29100',
         'mixins': ['PfRecordMixin'],
         'tree_root': True})

    pf_jurisdictions: Optional[list[str]] = Field(default=None, description="""The legal systems that apply to the record, in the organization's terms.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfFramework', 'PfActor']} })
    pf_organization: str = Field(default=..., description="""The organization that applies the framework.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfFramework']} })
    pf_ict_systems: Optional[list[str]] = Field(default=None, description="""The ICT systems the framework covers.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfFramework']} })
    pf_actors: Optional[list[Union[PfPiiPrincipal,PfPiiController,PfPiiProcessor,PfThirdParty]]] = Field(default=None, description="""Those who take part in handling the PII.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfFramework']} })
    pf_pii_items: Optional[list[PfPiiItem]] = Field(default=None, description="""The PII the organization has recognized.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfFramework']} })
    pf_flows: Optional[list[PfPiiFlow]] = Field(default=None, description="""The ways PII passes between the actors.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfFramework']} })
    pf_processing_activities: Optional[list[PfProcessingActivity]] = Field(default=None, description="""What the organization does with PII.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfFramework']} })
    pf_safeguarding_requirements: Optional[list[PfSafeguardingRequirement]] = Field(default=None, description="""What the organization must do to safeguard PII.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfFramework']} })
    pf_policies: Optional[list[PfPolicy]] = Field(default=None, description="""The organization's privacy policies.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfFramework']} })
    pf_controls: Optional[list[PfControl]] = Field(default=None, description="""The organization's controls.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfFramework']} })
    pf_principle_implementations: Optional[list[PfPrincipleImplementation]] = Field(default=None, description="""How the organization stands against each privacy principle.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfFramework']} })
    pf_risks: Optional[list[PfRisk]] = Field(default=None, description="""The risks to people that the organization has identified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfFramework']} })
    pf_impact_assessments: Optional[list[PfImpactAssessment]] = Field(default=None, description="""The organization's privacy impact assessments.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfFramework']} })
    pf_breaches: Optional[list[PfBreach]] = Field(default=None, description="""The breaches the organization has recorded.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfFramework']} })
    pf_consents: Optional[list[PfConsent]] = Field(default=None, description="""The consents the organization holds.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfFramework']} })
    pf_preferences: Optional[list[PfPreference]] = Field(default=None, description="""What people have said they prefer.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfFramework']} })
    pf_id: str = Field(default=..., description="""The record's identifier, unique among the records of the framework, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['PfRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['PfRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('pf_id')
    def pattern_pf_id(cls, v):
        pattern=re.compile(r"^\S+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid pf_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid pf_id format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class PfActor(PfRecordMixin):
    """
    Someone who takes part in handling PII, told apart by the part they play. One party can play different parts for different PII, with a record for each.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'annotations': {'iso29100_clause': {'tag': 'iso29100_clause', 'value': '5.2'}},
         'from_schema': 'https://w3id.org/lmodel/iso29100',
         'mixins': ['PfRecordMixin'],
         'slot_usage': {'pf_actor_type': {'name': 'pf_actor_type', 'required': True}}})

    pf_actor_type: Literal["PfActor"] = Field(default="PfActor", description="""The kind of actor: PfPiiPrincipal, PfPiiController, PfPiiProcessor or PfThirdParty.""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['PfActor']} })
    pf_jurisdictions: Optional[list[str]] = Field(default=None, description="""The legal systems that apply to the record, in the organization's terms.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfFramework', 'PfActor']} })
    pf_contact: Optional[str] = Field(default=None, description="""How to reach the actor about privacy.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfActor']} })
    pf_id: str = Field(default=..., description="""The record's identifier, unique among the records of the framework, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['PfRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['PfRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('pf_id')
    def pattern_pf_id(cls, v):
        pattern=re.compile(r"^\S+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid pf_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid pf_id format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class PfPiiPrincipal(PfActor):
    """
    The person the PII is about, or a group of such people when the organization records them together.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso29100_clause': {'tag': 'iso29100_clause', 'value': '5.2'}},
         'exact_mappings': ['dpv:DataSubject'],
         'from_schema': 'https://w3id.org/lmodel/iso29100'})

    pf_actor_type: Literal["PfPiiPrincipal"] = Field(default="PfPiiPrincipal", description="""The kind of actor: PfPiiPrincipal, PfPiiController, PfPiiProcessor or PfThirdParty.""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['PfActor']} })
    pf_jurisdictions: Optional[list[str]] = Field(default=None, description="""The legal systems that apply to the record, in the organization's terms.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfFramework', 'PfActor']} })
    pf_contact: Optional[str] = Field(default=None, description="""How to reach the actor about privacy.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfActor']} })
    pf_id: str = Field(default=..., description="""The record's identifier, unique among the records of the framework, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['PfRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['PfRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('pf_id')
    def pattern_pf_id(cls, v):
        pattern=re.compile(r"^\S+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid pf_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid pf_id format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class PfPiiController(PfActor):
    """
    The party that decides why and how PII is processed, and answers for it even when another party does the work.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso29100_clause': {'tag': 'iso29100_clause', 'value': '5.2'}},
         'exact_mappings': ['dpv:DataController'],
         'from_schema': 'https://w3id.org/lmodel/iso29100'})

    pf_purposes: Optional[list[str]] = Field(default=None, description="""The reasons the PII is processed, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfPiiController',
                       'PfProcessingActivity',
                       'PfPolicy',
                       'PfConsent']} })
    pf_legal_bases: Optional[list[str]] = Field(default=None, description="""What makes the processing lawful, in the terms of the law that applies.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfPiiController', 'PfProcessingActivity']} })
    pf_appointed_processors: Optional[list[str]] = Field(default=None, description="""The processors that work for the controller.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfPiiController']} })
    pf_controller_policy: Optional[str] = Field(default=None, description="""The privacy policy the controller works under.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfPiiController']} })
    pf_privacy_officer: Optional[str] = Field(default=None, description="""The person who advises the controller on privacy, where there is one.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfPiiController']} })
    pf_actor_type: Literal["PfPiiController"] = Field(default="PfPiiController", description="""The kind of actor: PfPiiPrincipal, PfPiiController, PfPiiProcessor or PfThirdParty.""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['PfActor']} })
    pf_jurisdictions: Optional[list[str]] = Field(default=None, description="""The legal systems that apply to the record, in the organization's terms.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfFramework', 'PfActor']} })
    pf_contact: Optional[str] = Field(default=None, description="""How to reach the actor about privacy.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfActor']} })
    pf_id: str = Field(default=..., description="""The record's identifier, unique among the records of the framework, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['PfRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['PfRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('pf_id')
    def pattern_pf_id(cls, v):
        pattern=re.compile(r"^\S+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid pf_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid pf_id format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class PfPiiProcessor(PfActor):
    """
    A party that processes PII for a controller, on that controller's instructions.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso29100_clause': {'tag': 'iso29100_clause', 'value': '5.2'}},
         'exact_mappings': ['dpv:DataProcessor'],
         'from_schema': 'https://w3id.org/lmodel/iso29100'})

    pf_instructing_controllers: Optional[list[str]] = Field(default=None, description="""The controllers whose instructions the processor follows.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfPiiProcessor']} })
    pf_processing_agreement: Optional[str] = Field(default=None, description="""The reference of the agreement that binds the processor, where there is one.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfPiiProcessor']} })
    pf_sub_processors: Optional[list[str]] = Field(default=None, description="""The processors this processor has engaged in turn.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfPiiProcessor']} })
    pf_actor_type: Literal["PfPiiProcessor"] = Field(default="PfPiiProcessor", description="""The kind of actor: PfPiiPrincipal, PfPiiController, PfPiiProcessor or PfThirdParty.""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['PfActor']} })
    pf_jurisdictions: Optional[list[str]] = Field(default=None, description="""The legal systems that apply to the record, in the organization's terms.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfFramework', 'PfActor']} })
    pf_contact: Optional[str] = Field(default=None, description="""How to reach the actor about privacy.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfActor']} })
    pf_id: str = Field(default=..., description="""The record's identifier, unique among the records of the framework, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['PfRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['PfRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('pf_id')
    def pattern_pf_id(cls, v):
        pattern=re.compile(r"^\S+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid pf_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid pf_id format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class PfThirdParty(PfActor):
    """
    A party outside the controller and its processors that receives PII for its own ends, and usually becomes a controller of that PII.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso29100_clause': {'tag': 'iso29100_clause', 'value': '5.2'}},
         'from_schema': 'https://w3id.org/lmodel/iso29100'})

    pf_receiving_purpose: Optional[str] = Field(default=None, description="""What the third party receives the PII for.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfThirdParty']} })
    pf_transfer_basis: Optional[str] = Field(default=None, description="""What makes the passing of PII to the third party lawful.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfThirdParty']} })
    pf_actor_type: Literal["PfThirdParty"] = Field(default="PfThirdParty", description="""The kind of actor: PfPiiPrincipal, PfPiiController, PfPiiProcessor or PfThirdParty.""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['PfActor']} })
    pf_jurisdictions: Optional[list[str]] = Field(default=None, description="""The legal systems that apply to the record, in the organization's terms.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfFramework', 'PfActor']} })
    pf_contact: Optional[str] = Field(default=None, description="""How to reach the actor about privacy.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfActor']} })
    pf_id: str = Field(default=..., description="""The record's identifier, unique among the records of the framework, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['PfRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['PfRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('pf_id')
    def pattern_pf_id(cls, v):
        pattern=re.compile(r"^\S+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid pf_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid pf_id format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class PfPiiItem(PfRecordMixin):
    """
    A piece or set of information that can be tied to a person, why it counts as PII, how sensitive it is and how it is handled.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso29100_clause': {'tag': 'iso29100_clause', 'value': '5.4'}},
         'comments': ["DPV's mapping says dpv:PersonalData is narrower than the "
                      "standard's PII, and this class keeps that direction."],
         'from_schema': 'https://w3id.org/lmodel/iso29100',
         'mixins': ['PfRecordMixin'],
         'narrow_mappings': ['dpv:PersonalData']})

    pf_concerned_principals: Optional[list[str]] = Field(default=None, description="""The people the PII of the record is about.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfPiiItem', 'PfRisk']} })
    pf_operations: Optional[list[PfOperation]] = Field(default=None, description="""The things done to the PII.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfPiiItem', 'PfProcessingActivity']} })
    pf_retention: Optional[str] = Field(default=None, description="""How long the PII is kept, as an ISO 8601 duration.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfPiiItem', 'PfProcessingActivity']} })
    pf_pii_categories: Optional[list[str]] = Field(default=None, description="""What the item holds, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfPiiItem']} })
    pf_recognized_by: Optional[list[PfPiiRecognition]] = Field(default=None, description="""Why the information counts as PII.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfPiiItem']} })
    pf_sensitivity: Optional[PfSensitivity] = Field(default=None, description="""How sensitive the item is.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfPiiItem']} })
    pf_pseudonymized: Optional[bool] = Field(default=None, description="""Whether an alias stands in for the item's identifying details.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfPiiItem']} })
    pf_linkability: Optional[str] = Field(default=None, description="""How easily the item could be joined with other data to identify someone, in the organization's words.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfPiiItem']} })
    pf_id: str = Field(default=..., description="""The record's identifier, unique among the records of the framework, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['PfRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['PfRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('pf_id')
    def pattern_pf_id(cls, v):
        pattern=re.compile(r"^\S+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid pf_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid pf_id format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class PfPiiFlow(PfRecordMixin):
    """
    One way PII passes from one actor to another, and who decides what happens to it afterwards.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso29100_clause': {'tag': 'iso29100_clause', 'value': '5.3'}},
         'from_schema': 'https://w3id.org/lmodel/iso29100',
         'mixins': ['PfRecordMixin']})

    pf_concerned_pii: Optional[list[str]] = Field(default=None, description="""The PII items the record concerns.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfPiiFlow',
                       'PfProcessingActivity',
                       'PfPolicy',
                       'PfRisk',
                       'PfBreach',
                       'PfConsent']} })
    pf_provider: str = Field(default=..., description="""The actor the PII comes from.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfPiiFlow']} })
    pf_recipient: str = Field(default=..., description="""The actor the PII goes to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfPiiFlow']} })
    pf_decides_afterwards: Optional[str] = Field(default=None, description="""The actor that decides what happens to the PII once it has passed. A processor never holds this position.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfPiiFlow']} })
    pf_id: str = Field(default=..., description="""The record's identifier, unique among the records of the framework, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['PfRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['PfRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('pf_id')
    def pattern_pf_id(cls, v):
        pattern=re.compile(r"^\S+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid pf_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid pf_id format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class PfProcessingActivity(PfRecordMixin):
    """
    Something the organization does with PII: why, on what basis, what it does to which PII, who is responsible, and how long the PII is kept.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ["The fields are what an adopter keeps. The framework's own "
                      'subject here is what counts as processing, which PfOperation '
                      'lists.'],
         'from_schema': 'https://w3id.org/lmodel/iso29100',
         'mixins': ['PfRecordMixin']})

    pf_purposes: Optional[list[str]] = Field(default=None, description="""The reasons the PII is processed, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfPiiController',
                       'PfProcessingActivity',
                       'PfPolicy',
                       'PfConsent']} })
    pf_legal_bases: Optional[list[str]] = Field(default=None, description="""What makes the processing lawful, in the terms of the law that applies.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfPiiController', 'PfProcessingActivity']} })
    pf_operations: Optional[list[PfOperation]] = Field(default=None, description="""The things done to the PII.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfPiiItem', 'PfProcessingActivity']} })
    pf_concerned_pii: Optional[list[str]] = Field(default=None, description="""The PII items the record concerns.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfPiiFlow',
                       'PfProcessingActivity',
                       'PfPolicy',
                       'PfRisk',
                       'PfBreach',
                       'PfConsent']} })
    pf_retention: Optional[str] = Field(default=None, description="""How long the PII is kept, as an ISO 8601 duration.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfPiiItem', 'PfProcessingActivity']} })
    pf_related_controls: Optional[list[str]] = Field(default=None, description="""The organization's controls that act on the record's subject.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfProcessingActivity', 'PfPrincipleImplementation', 'PfRisk']} })
    pf_controller: str = Field(default=..., description="""The controller that answers for the activity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfProcessingActivity']} })
    pf_processors: Optional[list[str]] = Field(default=None, description="""The processors that do the work.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfProcessingActivity']} })
    pf_activity_flows: Optional[list[str]] = Field(default=None, description="""The flows of PII the activity involves.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfProcessingActivity']} })
    pf_sensitivities: Optional[list[PfSensitivity]] = Field(default=None, description="""The levels of sensitivity among the PII involved.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfProcessingActivity']} })
    pf_crosses_borders: Optional[bool] = Field(default=None, description="""Whether PII leaves the jurisdiction it was collected in.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfProcessingActivity']} })
    pf_transfer_safeguards: Optional[list[str]] = Field(default=None, description="""What protects the PII when it crosses a border.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfProcessingActivity']} })
    pf_id: str = Field(default=..., description="""The record's identifier, unique among the records of the framework, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['PfRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['PfRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('pf_id')
    def pattern_pf_id(cls, v):
        pattern=re.compile(r"^\S+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid pf_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid pf_id format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class PfSafeguardingRequirement(PfRecordMixin):
    """
    Something the organization must do to protect PII, and where that duty comes from.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso29100_clause': {'tag': 'iso29100_clause', 'value': '5.5'}},
         'from_schema': 'https://w3id.org/lmodel/iso29100',
         'mixins': ['PfRecordMixin']})

    pf_requirement_factor: PfRequirementFactor = Field(default=..., description="""Where the requirement comes from.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfSafeguardingRequirement']} })
    pf_requirement_source: Optional[str] = Field(default=None, description="""The law, contract or other document that states it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfSafeguardingRequirement']} })
    pf_applies_to: Optional[list[str]] = Field(default=None, description="""The actors that must meet it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfSafeguardingRequirement']} })
    pf_met_by: Optional[list[str]] = Field(default=None, description="""The controls that meet it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfSafeguardingRequirement']} })
    pf_id: str = Field(default=..., description="""The record's identifier, unique among the records of the framework, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['PfRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['PfRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('pf_id')
    def pattern_pf_id(cls, v):
        pattern=re.compile(r"^\S+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid pf_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid pf_id format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class PfPolicy(PfRecordMixin):
    """
    A privacy policy: what the organization commits to about PII, written for its own people or as a notice to the people whose PII it handles.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso29100_clause': {'tag': 'iso29100_clause', 'value': '5.6'}},
         'from_schema': 'https://w3id.org/lmodel/iso29100',
         'mixins': ['PfRecordMixin']})

    pf_purposes: Optional[list[str]] = Field(default=None, description="""The reasons the PII is processed, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfPiiController',
                       'PfProcessingActivity',
                       'PfPolicy',
                       'PfConsent']} })
    pf_concerned_pii: Optional[list[str]] = Field(default=None, description="""The PII items the record concerns.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfPiiFlow',
                       'PfProcessingActivity',
                       'PfPolicy',
                       'PfRisk',
                       'PfBreach',
                       'PfConsent']} })
    pf_principles: Optional[list[PfPrinciple]] = Field(default=None, description="""The privacy principles the record bears on.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfPolicy', 'PfControl']} })
    pf_policy_audience: PfPolicyAudience = Field(default=..., description="""Who the policy is written for.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfPolicy']} })
    pf_policy_version: Optional[str] = Field(default=None, description="""The version of the policy.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfPolicy']} })
    pf_policy_scope: Optional[str] = Field(default=None, description="""What the policy covers.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfPolicy']} })
    pf_policy_effective_date: Optional[date] = Field(default=None, description="""When the policy takes effect.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfPolicy']} })
    pf_policy_last_reviewed: Optional[date] = Field(default=None, description="""When the policy was last reviewed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfPolicy']} })
    pf_retention_statement: Optional[str] = Field(default=None, description="""What the policy says about how long PII is kept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfPolicy']} })
    pf_stated_rights: Optional[list[str]] = Field(default=None, description="""The rights the policy tells people they have.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfPolicy']} })
    pf_inquiry_contact: Optional[str] = Field(default=None, description="""Where people can send questions about the policy.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfPolicy']} })
    pf_id: str = Field(default=..., description="""The record's identifier, unique among the records of the framework, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['PfRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['PfRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('pf_id')
    def pattern_pf_id(cls, v):
        pattern=re.compile(r"^\S+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid pf_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid pf_id format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class PfControl(PfRecordMixin):
    """
    A measure that treats a privacy risk by making it less likely or less harmful, the principles it serves and how far it has been put into effect.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso29100_clause': {'tag': 'iso29100_clause', 'value': '5.7'}},
         'from_schema': 'https://w3id.org/lmodel/iso29100',
         'mixins': ['PfRecordMixin']})

    pf_principles: Optional[list[PfPrinciple]] = Field(default=None, description="""The privacy principles the record bears on.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfPolicy', 'PfControl']} })
    pf_evidence: Optional[list[str]] = Field(default=None, description="""What shows that the record's claim holds, such as a report or a log.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfControl', 'PfPrincipleImplementation', 'PfConsent']} })
    pf_control_kind: PfControlKind = Field(default=..., description="""The form the control takes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfControl']} })
    pf_control_objective: Optional[str] = Field(default=None, description="""What the control is meant to achieve.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfControl']} })
    pf_control_detail: Optional[str] = Field(default=None, description="""How the control is put into effect.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfControl']} })
    pf_control_responsible: Optional[str] = Field(default=None, description="""The actor that answers for the control.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfControl']} })
    pf_control_state: Optional[PfImplementationState] = Field(default=None, description="""How far the control has been put into effect.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfControl']} })
    pf_answers_requirements: Optional[list[str]] = Field(default=None, description="""The safeguarding requirements the control answers to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfControl']} })
    pf_id: str = Field(default=..., description="""The record's identifier, unique among the records of the framework, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['PfRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['PfRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('pf_id')
    def pattern_pf_id(cls, v):
        pattern=re.compile(r"^\S+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid pf_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid pf_id format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class PfPrincipleImplementation(PfRecordMixin):
    """
    How the organization stands against one privacy principle: what it does, what shows it, and what is still missing.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso29100_clause': {'tag': 'iso29100_clause', 'value': '6.1'}},
         'from_schema': 'https://w3id.org/lmodel/iso29100',
         'mixins': ['PfRecordMixin']})

    pf_related_controls: Optional[list[str]] = Field(default=None, description="""The organization's controls that act on the record's subject.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfProcessingActivity', 'PfPrincipleImplementation', 'PfRisk']} })
    pf_evidence: Optional[list[str]] = Field(default=None, description="""What shows that the record's claim holds, such as a report or a log.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfControl', 'PfPrincipleImplementation', 'PfConsent']} })
    pf_principle: PfPrinciple = Field(default=..., description="""The principle the record is about.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfPrincipleImplementation']} })
    pf_measures: Optional[list[str]] = Field(default=None, description="""What the organization does to follow the principle.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfPrincipleImplementation']} })
    pf_gaps: Optional[list[str]] = Field(default=None, description="""Where the organization falls short.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfPrincipleImplementation']} })
    pf_improvements: Optional[list[str]] = Field(default=None, description="""What the organization will do about the gaps.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfPrincipleImplementation']} })
    pf_last_assessed: Optional[date] = Field(default=None, description="""When the organization last checked its standing.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfPrincipleImplementation']} })
    pf_id: str = Field(default=..., description="""The record's identifier, unique among the records of the framework, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['PfRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['PfRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('pf_id')
    def pattern_pf_id(cls, v):
        pattern=re.compile(r"^\S+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid pf_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid pf_id format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class PfRisk(PfRecordMixin):
    """
    A way that handling PII could harm people: where the risk comes from, how likely and how bad it is, and what is done about it.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['The framework names privacy risk as an idea and leaves the '
                      'scale to the organization. These fields are what an adopter '
                      'keeps.'],
         'from_schema': 'https://w3id.org/lmodel/iso29100',
         'mixins': ['PfRecordMixin']})

    pf_concerned_pii: Optional[list[str]] = Field(default=None, description="""The PII items the record concerns.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfPiiFlow',
                       'PfProcessingActivity',
                       'PfPolicy',
                       'PfRisk',
                       'PfBreach',
                       'PfConsent']} })
    pf_concerned_principals: Optional[list[str]] = Field(default=None, description="""The people the PII of the record is about.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfPiiItem', 'PfRisk']} })
    pf_related_controls: Optional[list[str]] = Field(default=None, description="""The organization's controls that act on the record's subject.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfProcessingActivity', 'PfPrincipleImplementation', 'PfRisk']} })
    pf_risk_source: Optional[str] = Field(default=None, description="""Where the risk comes from.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfRisk']} })
    pf_risk_likelihood: Optional[str] = Field(default=None, description="""How likely the harm is, in the organization's own terms.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfRisk']} })
    pf_risk_consequence: Optional[str] = Field(default=None, description="""What the harm to people would be.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfRisk']} })
    pf_risk_inherent_level: Optional[PfRiskLevel] = Field(default=None, description="""The risk's level before controls.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfRisk']} })
    pf_risk_residual_level: Optional[PfRiskLevel] = Field(default=None, description="""The risk's level after controls, which is never above the level before.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfRisk']} })
    pf_risk_owner: Optional[str] = Field(default=None, description="""The person who answers for the risk.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfRisk']} })
    pf_id: str = Field(default=..., description="""The record's identifier, unique among the records of the framework, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['PfRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['PfRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('pf_id')
    def pattern_pf_id(cls, v):
        pattern=re.compile(r"^\S+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid pf_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid pf_id format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class PfImpactAssessment(PfRecordMixin):
    """
    A review of what a system or activity could do to people's privacy, the risks it found and what became of them.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['These fields are what an adopter keeps, and go beyond the '
                      'framework itself.'],
         'from_schema': 'https://w3id.org/lmodel/iso29100',
         'mixins': ['PfRecordMixin']})

    pf_assessment_scope: Optional[str] = Field(default=None, description="""What the assessment looks at.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfImpactAssessment']} })
    pf_assessment_date: Optional[date] = Field(default=None, description="""When the assessment was done.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfImpactAssessment']} })
    pf_assessor: Optional[str] = Field(default=None, description="""Who did the assessment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfImpactAssessment']} })
    pf_assessed_activities: Optional[list[str]] = Field(default=None, description="""The processing activities it looks at.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfImpactAssessment']} })
    pf_risks_found: Optional[list[str]] = Field(default=None, description="""The risks it found.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfImpactAssessment']} })
    pf_risks_treated: Optional[list[str]] = Field(default=None, description="""Those of the risks found that have been treated.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfImpactAssessment']} })
    pf_risks_accepted: Optional[list[str]] = Field(default=None, description="""Those of the risks found that the organization has accepted as they stand.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfImpactAssessment']} })
    pf_assessment_outcome: Optional[str] = Field(default=None, description="""What the assessment concluded.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfImpactAssessment']} })
    pf_consultations: Optional[list[str]] = Field(default=None, description="""Who was asked, and what they said.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfImpactAssessment']} })
    pf_next_assessment: Optional[date] = Field(default=None, description="""When the next assessment is due, which is after this one.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfImpactAssessment']} })
    pf_id: str = Field(default=..., description="""The record's identifier, unique among the records of the framework, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['PfRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['PfRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('pf_id')
    def pattern_pf_id(cls, v):
        pattern=re.compile(r"^\S+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid pf_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid pf_id format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class PfBreach(PfRecordMixin):
    """
    A time when PII was handled against a safeguarding requirement: what happened, who was told and what was done.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['The framework names the idea of a breach. These fields are what '
                      'an adopter keeps, and go beyond the framework itself.'],
         'from_schema': 'https://w3id.org/lmodel/iso29100',
         'mixins': ['PfRecordMixin']})

    pf_concerned_pii: Optional[list[str]] = Field(default=None, description="""The PII items the record concerns.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfPiiFlow',
                       'PfProcessingActivity',
                       'PfPolicy',
                       'PfRisk',
                       'PfBreach',
                       'PfConsent']} })
    pf_breach_occurred: Optional[datetime ] = Field(default=None, description="""When the breach happened.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfBreach']} })
    pf_breach_discovered: Optional[datetime ] = Field(default=None, description="""When the organization found out, which is not before it happened.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfBreach']} })
    pf_breach_closed: Optional[datetime ] = Field(default=None, description="""When the organization closed the matter, which is not before it found out.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfBreach']} })
    pf_principals_affected: Optional[int] = Field(default=None, description="""How many people the breach reached, where that is known.""", ge=1, json_schema_extra = { "linkml_meta": {'domain_of': ['PfBreach']} })
    pf_breached_requirements: Optional[list[str]] = Field(default=None, description="""The safeguarding requirements the breach went against.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfBreach']} })
    pf_breach_severity: Optional[PfRiskLevel] = Field(default=None, description="""How serious the breach is.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfBreach']} })
    pf_immediate_actions: Optional[list[str]] = Field(default=None, description="""What was done straight away.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfBreach']} })
    pf_notification_required: Optional[bool] = Field(default=None, description="""Whether a law or contract requires anyone to be told.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfBreach']} })
    pf_notifications: Optional[list[str]] = Field(default=None, description="""Who was told, and when.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfBreach']} })
    pf_remediation: Optional[list[str]] = Field(default=None, description="""What was done to put things right.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfBreach']} })
    pf_lessons: Optional[str] = Field(default=None, description="""What the organization learned.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfBreach']} })
    pf_id: str = Field(default=..., description="""The record's identifier, unique among the records of the framework, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['PfRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['PfRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('pf_id')
    def pattern_pf_id(cls, v):
        pattern=re.compile(r"^\S+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid pf_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid pf_id format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class PfConsent(PfRecordMixin):
    """
    One person's agreement to the processing of their PII for stated purposes, and where it stands.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['The framework defines consent and its principle, and DPV maps '
                      'that term to dpv:InformedConsent. The fields are what an '
                      'adopter keeps, and go beyond the framework itself.'],
         'exact_mappings': ['dpv:InformedConsent'],
         'from_schema': 'https://w3id.org/lmodel/iso29100',
         'mixins': ['PfRecordMixin'],
         'rules': [{'description': 'A consent with a withdrawal date has the state '
                                   'withdrawn.',
                    'postconditions': {'slot_conditions': {'pf_consent_state': {'equals_string': 'withdrawn',
                                                                                'name': 'pf_consent_state'}}},
                    'preconditions': {'slot_conditions': {'pf_consent_withdrawn': {'name': 'pf_consent_withdrawn',
                                                                                   'value_presence': 'PRESENT'}}},
                    'title': 'a withdrawal date means the consent is withdrawn'}],
         'slot_usage': {'pf_principal': {'name': 'pf_principal', 'required': True}}})

    pf_purposes: Optional[list[str]] = Field(default=None, description="""The reasons the PII is processed, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfPiiController',
                       'PfProcessingActivity',
                       'PfPolicy',
                       'PfConsent']} })
    pf_concerned_pii: Optional[list[str]] = Field(default=None, description="""The PII items the record concerns.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfPiiFlow',
                       'PfProcessingActivity',
                       'PfPolicy',
                       'PfRisk',
                       'PfBreach',
                       'PfConsent']} })
    pf_evidence: Optional[list[str]] = Field(default=None, description="""What shows that the record's claim holds, such as a report or a log.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfControl', 'PfPrincipleImplementation', 'PfConsent']} })
    pf_principal: str = Field(default=..., description="""The person the record is about.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfConsent', 'PfPreference']} })
    pf_consent_mechanism: Optional[PfConsentMechanism] = Field(default=None, description="""How the agreement was obtained.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfConsent']} })
    pf_consent_given: Optional[datetime ] = Field(default=None, description="""When the person agreed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfConsent']} })
    pf_consent_state: PfConsentState = Field(default=..., description="""Where the agreement stands.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfConsent']} })
    pf_consent_withdrawn: Optional[datetime ] = Field(default=None, description="""When the person took the agreement back.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfConsent']} })
    pf_id: str = Field(default=..., description="""The record's identifier, unique among the records of the framework, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['PfRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['PfRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('pf_id')
    def pattern_pf_id(cls, v):
        pattern=re.compile(r"^\S+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid pf_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid pf_id format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class PfPreference(PfRecordMixin):
    """
    What one person has said they want done, or not done, with their PII.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['The framework names the idea of a privacy preference. These '
                      'fields are what an adopter keeps, and go beyond the framework '
                      'itself.'],
         'from_schema': 'https://w3id.org/lmodel/iso29100',
         'mixins': ['PfRecordMixin'],
         'slot_usage': {'pf_principal': {'name': 'pf_principal', 'required': True}}})

    pf_principal: str = Field(default=..., description="""The person the record is about.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfConsent', 'PfPreference']} })
    pf_preference_scope: Optional[str] = Field(default=None, description="""What the preference applies to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfPreference']} })
    pf_wants_anonymity: Optional[bool] = Field(default=None, description="""Whether the person asks not to be identified at all.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfPreference']} })
    pf_wants_pseudonymity: Optional[bool] = Field(default=None, description="""Whether the person asks to appear under an alias.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfPreference']} })
    pf_refused_operations: Optional[list[PfOperation]] = Field(default=None, description="""What the person does not want done to their PII.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfPreference']} })
    pf_refused_recipients: Optional[list[str]] = Field(default=None, description="""Who the person does not want their PII passed to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfPreference']} })
    pf_preference_recorded: Optional[date] = Field(default=None, description="""When the organization recorded the preference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfPreference']} })
    pf_id: str = Field(default=..., description="""The record's identifier, unique among the records of the framework, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PfRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['PfRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['PfRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('pf_id')
    def pattern_pf_id(cls, v):
        pattern=re.compile(r"^\S+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid pf_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid pf_id format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
PfRecordMixin.model_rebuild()
PfFramework.model_rebuild()
PfActor.model_rebuild()
PfPiiPrincipal.model_rebuild()
PfPiiController.model_rebuild()
PfPiiProcessor.model_rebuild()
PfThirdParty.model_rebuild()
PfPiiItem.model_rebuild()
PfPiiFlow.model_rebuild()
PfProcessingActivity.model_rebuild()
PfSafeguardingRequirement.model_rebuild()
PfPolicy.model_rebuild()
PfControl.model_rebuild()
PfPrincipleImplementation.model_rebuild()
PfRisk.model_rebuild()
PfImpactAssessment.model_rebuild()
PfBreach.model_rebuild()
PfConsent.model_rebuild()
PfPreference.model_rebuild()
