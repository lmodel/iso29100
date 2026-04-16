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


metamodel_version = "1.7.0"
version = "1.0.0"


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


linkml_meta = LinkMLMeta({'annotations': {'previous_edition': {'tag': 'previous_edition',
                                          'value': 'ISO/IEC 29100:2011/Amd 1:2018'},
                     'rights_notice': {'tag': 'rights_notice',
                                       'value': 'This project is licensed under '
                                                'Apache-2.0 for original code and '
                                                'schema structure. ISO/IEC '
                                                'standards text is owned by ISO '
                                                'and is not redistributed by this '
                                                'project license.'},
                     'schema_maintainer': {'tag': 'schema_maintainer',
                                           'value': 'noel.mcloughlin@gmail.com'},
                     'schema_status': {'tag': 'schema_status', 'value': 'stable'},
                     'standard_date': {'tag': 'standard_date', 'value': '2024-02'},
                     'standard_edition': {'tag': 'standard_edition',
                                          'value': 'Second edition'},
                     'standard_reference': {'tag': 'standard_reference',
                                            'value': 'ISO/IEC 29100:2024(E)'},
                     'standard_title': {'tag': 'standard_title',
                                        'value': 'Information technology — '
                                                 'Security techniques — Privacy '
                                                 'framework'}},
     'default_prefix': 'iso29100',
     'default_range': 'string',
     'description': 'A comprehensive LinkML schema modeling the ISO/IEC 29100:2024 '
                    'privacy framework for information and communication '
                    'technology (ICT) systems. Captures actors and roles, PII '
                    'recognition, privacy safeguarding requirements, the eleven '
                    'privacy principles, and the privacy risk management process.\n'
                    'This schema covers: - Privacy framework actors (PII '
                    'principal, controller, processor, third party) - Personally '
                    'identifiable information (PII) and its categories - Privacy '
                    'principles (11 principles from Clause 6) - Privacy '
                    'safeguarding requirements and influencing factors - Privacy '
                    'risk management including privacy impact assessment - Privacy '
                    'policies, privacy controls, consent records, and privacy '
                    'preferences',
     'id': 'https://w3id.org/lmodel/iso29100',
     'imports': ['linkml:types'],
     'license': 'https://www.apache.org/licenses/LICENSE-2.0',
     'name': 'iso29100',
     'prefixes': {'dcterms': {'prefix_prefix': 'dcterms',
                              'prefix_reference': 'http://purl.org/dc/terms/'},
                  'dpv': {'prefix_prefix': 'dpv',
                          'prefix_reference': 'https://w3id.org/dpv#'},
                  'iso27001': {'prefix_prefix': 'iso27001',
                               'prefix_reference': 'https://w3id.org/lmodel/iso27001/'},
                  'iso29100': {'prefix_prefix': 'iso29100',
                               'prefix_reference': 'https://w3id.org/lmodel/iso29100/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'rdfs': {'prefix_prefix': 'rdfs',
                           'prefix_reference': 'http://www.w3.org/2000/01/rdf-schema#'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'}},
     'see_also': ['https://www.iso.org/standard/85938.html',
                  'https://dev.dpvcg.org/mappings/iso/'],
     'source_file': 'src/iso29100/schema/iso29100.yaml',
     'subsets': {'pii_recognition': {'description': 'Elements relating to '
                                                    'recognizing and categorizing '
                                                    'personally identifiable '
                                                    'information, including '
                                                    'identifiers, sensitivity, and '
                                                    'pseudonymization (Clause '
                                                    '5.4).',
                                     'from_schema': 'https://w3id.org/lmodel/iso29100',
                                     'name': 'pii_recognition'},
                 'privacy_framework_core': {'comments': ['Covers the fundamental '
                                                         'building blocks of the '
                                                         'privacy framework'],
                                            'description': 'Core privacy framework '
                                                           'elements: actors, '
                                                           'roles, PII concept, '
                                                           'interactions, and the '
                                                           'overall framework '
                                                           'container (Clauses '
                                                           '5.1-5.3).',
                                            'from_schema': 'https://w3id.org/lmodel/iso29100',
                                            'name': 'privacy_framework_core'},
                 'privacy_governance': {'description': 'Privacy policies, privacy '
                                                       'controls, and governance '
                                                       'elements that implement '
                                                       'safeguarding requirements '
                                                       '(Clauses 5.6-5.7).',
                                        'from_schema': 'https://w3id.org/lmodel/iso29100',
                                        'name': 'privacy_governance'},
                 'privacy_principles': {'annotations': {'principle_count': {'tag': 'principle_count',
                                                                            'value': '11'}},
                                        'description': 'The eleven privacy '
                                                       'principles defined in '
                                                       'Clause 6 of ISO/IEC '
                                                       '29100:2024. These '
                                                       'principles guide the '
                                                       'design and operation of '
                                                       'privacy programs.',
                                        'from_schema': 'https://w3id.org/lmodel/iso29100',
                                        'name': 'privacy_principles'},
                 'privacy_risk_management': {'description': 'Elements supporting '
                                                            'privacy risk '
                                                            'management, including '
                                                            'privacy impact '
                                                            'assessments and '
                                                            'privacy risk '
                                                            'treatment (Clauses '
                                                            '3.17-3.18, 5.5).',
                                             'from_schema': 'https://w3id.org/lmodel/iso29100',
                                             'name': 'privacy_risk_management'},
                 'privacy_safeguarding': {'description': 'Privacy safeguarding '
                                                         'requirements and their '
                                                         'influencing factors: '
                                                         'legal, regulatory, '
                                                         'contractual, business, '
                                                         'and other factors '
                                                         '(Clause 5.5).',
                                          'from_schema': 'https://w3id.org/lmodel/iso29100',
                                          'name': 'privacy_safeguarding'}},
     'title': 'ISO 29100 / Privacy Framework: LinkML Schema',
     'types': {'duration_type': {'base': 'str',
                                 'description': 'ISO 8601 duration value such as '
                                                'P1Y, P30D, or PT4H.',
                                 'from_schema': 'https://w3id.org/lmodel/iso29100',
                                 'name': 'duration_type',
                                 'uri': 'xsd:duration'},
               'positive_integer_type': {'base': 'int',
                                         'description': 'Integer greater than '
                                                        'zero; natural number '
                                                        'explicitly excluding '
                                                        'zero.',
                                         'from_schema': 'https://w3id.org/lmodel/iso29100',
                                         'name': 'positive_integer_type',
                                         'uri': 'xsd:positiveInteger'}}} )

class PrivacyPrinciple(str, Enum):
    """
    The eleven privacy principles defined in ISO/IEC 29100:2024 Clause 6 that govern the processing of PII in ICT systems.
    """
    consent_and_choice = "consent_and_choice"
    """
    Schema value for privacy principle 1 (Clause 6.2): the organization gives PII principals meaningful choice over processing of their PII, manages opt-in consent mechanisms, and provides readily accessible means to withdraw consent.
    """
    purpose_legitimacy_and_specification = "purpose_legitimacy_and_specification"
    """
    Schema value for privacy principle 2 (Clause 6.3): the organization ensures each processing purpose is lawful, relies on a valid legal basis, and is communicated to PII principals prior to or at the time of collection.
    """
    collection_limitation = "collection_limitation"
    """
    Schema value for privacy principle 3 (Clause 6.4): the organization limits PII collection to what is lawful and strictly necessary to fulfil the stated processing purposes.
    """
    data_minimization = "data_minimization"
    """
    Schema value for privacy principle 4 (Clause 6.5): the organization designs processing procedures and ICT systems to minimize the volume of PII handled and the number of parties with access to it.
    """
    use_retention_and_disclosure_limitation = "use_retention_and_disclosure_limitation"
    """
    Schema value for privacy principle 5 (Clause 6.6): the organization limits use, retention, and disclosure of PII to the minimum needed for legitimate purposes, and securely disposes of PII once those purposes have been fulfilled.
    """
    accuracy_and_quality = "accuracy_and_quality"
    """
    Schema value for privacy principle 6 (Clause 6.7): the organization ensures PII is accurate, complete, current, and fit for purpose, and establishes procedures for verification, correction, and ongoing quality control of processed PII.
    """
    openness_transparency_and_notice = "openness_transparency_and_notice"
    """
    Schema value for privacy principle 7 (Clause 6.8): the organization provides PII principals with clear, accessible information about its PII processing policies and practices, and notifies them of material changes to those policies.
    """
    individual_participation_and_access = "individual_participation_and_access"
    """
    Schema value for privacy principle 8 (Clause 6.9): the organization gives PII principals the ability to access and review their PII and to challenge its accuracy and completeness, subject to applicable law.
    """
    accountability = "accountability"
    """
    Schema value for privacy principle 9 (Clause 6.10): the organization documents and communicates its privacy obligations, ensures equivalent protection when transferring PII to third parties, and maintains internal complaint-handling and redress procedures.
    """
    information_security = "information_security"
    """
    Schema value for privacy principle 10 (Clause 6.11): the organization applies appropriate security controls across operational, functional, and strategic levels to protect PII against unauthorized access, loss, or misuse throughout its full lifecycle.
    """
    privacy_compliance = "privacy_compliance"
    """
    Schema value for privacy principle 11 (Clause 6.12): the organization verifies and demonstrates compliance with data protection and privacy requirements through audits, independent internal controls, and ongoing privacy risk assessments.
    """


class PIIFlowRole(str, Enum):
    """
    The role played by an actor in a specific PII flow scenario, as described in Table 1 of ISO/IEC 29100:2024 Clause 5.3.
    """
    pii_provider = "pii_provider"
    """
    Actor that provides PII to another party in this flow scenario.
    """
    pii_recipient = "pii_recipient"
    """
    Actor that receives PII from another party in this flow scenario.
    """
    not_involved = "not_involved"
    """
    Actor not directly involved in this specific PII flow scenario.
    """


class PIIProcessingOperation(str, Enum):
    """
    Categories of operations that can be performed on PII, as referenced in the definition of processing of PII (Clause 3.21).
    """
    collection = "collection"
    """
    Gathering or acquiring PII from PII principals or other sources.
    """
    storage = "storage"
    """
    Storing PII in a persistent manner in ICT systems or other media.
    """
    alteration = "alteration"
    """
    Modifying or updating existing PII.
    """
    retrieval = "retrieval"
    """
    Accessing or fetching stored PII for use.
    """
    consultation = "consultation"
    """
    Reviewing or examining PII without necessarily extracting it.
    """
    disclosure = "disclosure"
    """
    Making PII available to other parties or making it accessible.
    """
    anonymization = "anonymization"
    """
    Irreversibly altering PII such that the PII principal can no longer be identified directly or indirectly.
    """
    pseudonymization = "pseudonymization"
    """
    Replacing identifying information in PII with an alias, retaining linkability while restricting direct identification.
    """
    dissemination = "dissemination"
    """
    Widely distributing or publishing PII to multiple recipients.
    """
    deletion = "deletion"
    """
    Removing PII such that it is no longer accessible or usable.
    """
    destruction = "destruction"
    """
    Permanently and irrecoverably eliminating PII and its carriers.
    """


class SafeguardingRequirementFactor(str, Enum):
    """
    Categories of factors that influence an organization's privacy safeguarding requirements, as described in Clause 5.5 and Figure 1.
    """
    legal_and_regulatory = "legal_and_regulatory"
    """
    Safeguarding requirements arising from applicable laws (international, national, and local), regulations, judicial decisions, and negotiated labour or work-council agreements.
    """
    contractual = "contractual"
    """
    Safeguarding requirements set out in data processing agreements, company policies, and binding corporate rules agreed between PII controllers, processors, and other parties.
    """
    business = "business"
    """
    Safeguarding requirements driven by the application's characteristics, industry guidelines, codes of conduct, or standards voluntarily adopted by the organization as part of its business model.
    """
    other = "other"
    """
    Safeguarding requirements arising from PII principal privacy preferences, internal control frameworks, or technical standards voluntarily adopted by the organization.
    """


class PIISensitivityCategory(str, Enum):
    """
    Categories of PII based on sensitivity, distinguishing standard PII from sensitive PII as defined in Clause 3.23.
    """
    standard = "standard"
    """
    PII that does not meet the threshold for sensitive PII but still requires appropriate privacy protection measures.
    """
    sensitive = "sensitive"
    """
    PII warranting heightened protection due to its potential for significant adverse impact on the individual, or because applicable law classifies it as a special category. Typical examples include health, biometric, financial, racial, religious, political, and sexual orientation data. Processing may require opt-in consent or specific legal authorization.
    """


class ConsentMechanism(str, Enum):
    """
    The mechanism by which a PII principal provides or withholds consent for PII processing, as referenced in Clauses 3.6 and 6.2.
    """
    opt_in = "opt_in"
    """
    The PII principal must take an explicit action to express prior consent for their PII to be processed for a particular purpose.
    """
    opt_out = "opt_out"
    """
    The PII principal must take a separate action to withhold or withdraw consent; processing is presumed permitted unless that action is taken.
    """
    implied = "implied"
    """
    Consent implied by some action of the PII principal, such as placing an order or using a service, where applicable law permits.
    """


class PrivacyRiskLevel(str, Enum):
    """
    Qualitative assessment of privacy risk level based on likelihood and potential adverse consequences for PII principals.
    """
    low = "low"
    """
    Limited potential adverse consequences for PII principals.
    """
    medium = "medium"
    """
    Moderate risk requiring management attention and planned controls.
    """
    high = "high"
    """
    Significant risk with potentially serious consequences for PII principals.
    """
    very_high = "very_high"
    """
    Severe risk with potentially catastrophic or irreversible consequences for PII principals requiring immediate treatment.
    """


class PrivacyControlType(str, Enum):
    """
    Categories of privacy controls that treat privacy risks by reducing their likelihood or consequences, as noted in Clause 3.12 Note 1.
    """
    organizational = "organizational"
    """
    Policies, procedures, guidelines, management practices, or organizational structures used as privacy controls.
    """
    physical = "physical"
    """
    Physical measures protecting PII and PII processing infrastructure.
    """
    technical = "technical"
    """
    ICT measures, products, or services that protect privacy, including privacy enhancing technologies (PETs).
    """
    legal_contractual = "legal_contractual"
    """
    Legal contracts, binding corporate rules, or data processing agreements implementing privacy safeguards.
    """



class NamedEntity(ConfiguredBaseModel):
    """
    Abstract base class for all entities with a unique identifier, name, and description. Provides common identification and documentation slots.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'comments': ['All concrete classes should inherit from this or a subclass',
                      'Ensures consistent identification across the schema'],
         'from_schema': 'https://w3id.org/lmodel/iso29100',
         'slot_usage': {'id': {'description': 'Unique identifier for this entity '
                                              'instance.',
                               'identifier': True,
                               'name': 'id',
                               'required': True}}})

    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'examples': [{'value': 'iso29100:framework-acme-corp'},
                      {'value': 'iso29100:pii-controller-001'}],
         'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Should provide sufficient detail for understanding without '
                      'external reference'],
         'domain_of': ['NamedEntity'],
         'slot_uri': 'dcterms:description'} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity record was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:created'} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity record was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:modified'} })


class PrivacyFramework(NamedEntity):
    """
    Top-level container representing an organization's privacy framework for protecting PII within ICT systems.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso29100_clause': {'tag': 'iso29100_clause', 'value': '5.1'}},
         'comments': ['Root entity for any ISO 29100 conformance dataset',
                      'Aggregates all privacy framework components and their '
                      'relationships',
                      'Reference: ISO/IEC 29100:2024 Clause 5.1. ISO/IEC standards '
                      'text is copyright ISO - not reproduced here.'],
         'from_schema': 'https://w3id.org/lmodel/iso29100',
         'in_subset': ['privacy_framework_core'],
         'related_mappings': ['iso27001:InformationSecurityManagementSystem'],
         'tree_root': True})

    organization_name: Optional[str] = Field(default=None, description="""Name of the organization operating the privacy framework.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso29100_clause': {'tag': 'iso29100_clause', 'value': '5.1'}},
         'domain_of': ['PrivacyFramework']} })
    ict_system_description: Optional[str] = Field(default=None, description="""Description of the ICT system(s) within the scope of the privacy framework.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrivacyFramework']} })
    applicable_jurisdictions: Optional[list[str]] = Field(default=None, description="""Legal jurisdictions whose privacy laws apply to the organization.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrivacyFramework']} })
    pii_controllers: Optional[list[PIIController]] = Field(default=None, description="""PII controllers operating within this privacy framework.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrivacyFramework']} })
    pii_processors: Optional[list[PIIProcessor]] = Field(default=None, description="""PII processors engaged within this privacy framework.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrivacyFramework']} })
    third_parties: Optional[list[ThirdParty]] = Field(default=None, description="""Third parties that may receive PII within this framework.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrivacyFramework']} })
    pii_principals_description: Optional[str] = Field(default=None, description="""Description of the categories of PII principals whose PII is processed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrivacyFramework']} })
    privacy_policy: Optional[str] = Field(default=None, description="""The organization's privacy policy governing PII processing.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso29100_clause': {'tag': 'iso29100_clause', 'value': '5.6'}},
         'domain_of': ['PrivacyFramework']} })
    privacy_controls: Optional[list[PrivacyControl]] = Field(default=None, description="""Privacy controls implemented within the framework.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso29100_clause': {'tag': 'iso29100_clause', 'value': '5.7'}},
         'domain_of': ['PrivacyFramework']} })
    safeguarding_requirements: Optional[list[PrivacySafeguardingRequirement]] = Field(default=None, description="""Privacy safeguarding requirements applicable to the organization.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso29100_clause': {'tag': 'iso29100_clause', 'value': '5.5'}},
         'domain_of': ['PrivacyFramework']} })
    privacy_risks: Optional[list[PrivacyRisk]] = Field(default=None, description="""Privacy risks identified within the framework scope.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrivacyFramework']} })
    privacy_impact_assessments: Optional[list[PrivacyImpactAssessment]] = Field(default=None, description="""Privacy impact assessments conducted under this framework.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrivacyFramework']} })
    privacy_breaches: Optional[list[PrivacyBreach]] = Field(default=None, description="""Privacy breaches recorded within the framework.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrivacyFramework']} })
    pii_processing_activities: Optional[list[PIIProcessingActivity]] = Field(default=None, description="""PII processing activities within the framework scope.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrivacyFramework']} })
    principle_implementations: Optional[list[PrivacyPrincipleImplementation]] = Field(default=None, description="""Implementation records for each of the eleven privacy principles.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrivacyFramework']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'examples': [{'value': 'iso29100:framework-acme-corp'},
                      {'value': 'iso29100:pii-controller-001'}],
         'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Should provide sufficient detail for understanding without '
                      'external reference'],
         'domain_of': ['NamedEntity'],
         'slot_uri': 'dcterms:description'} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity record was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:created'} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity record was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:modified'} })


class PrivacyStakeholder(NamedEntity):
    """
    Schema base class for the four actor types recognized by the privacy framework: PII principals, PII controllers, PII processors, and third parties. Provides shared contact and jurisdictional attributes common to all stakeholder roles.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'annotations': {'iso29100_clause': {'tag': 'iso29100_clause',
                                             'value': '3.20'}},
         'comments': ['Reference: ISO/IEC 29100:2024 Clause 3.20. ISO/IEC standards '
                      'text is copyright ISO - not reproduced here.'],
         'exact_mappings': ['dpv:Entity'],
         'from_schema': 'https://w3id.org/lmodel/iso29100',
         'in_subset': ['privacy_framework_core'],
         'related_mappings': ['iso27001:InterestedParty']})

    contact_information: Optional[str] = Field(default=None, description="""Contact details for the privacy stakeholder.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrivacyStakeholder']} })
    jurisdictions: Optional[list[str]] = Field(default=None, description="""Jurisdictions in which the privacy stakeholder operates.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrivacyStakeholder']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'examples': [{'value': 'iso29100:framework-acme-corp'},
                      {'value': 'iso29100:pii-controller-001'}],
         'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Should provide sufficient detail for understanding without '
                      'external reference'],
         'domain_of': ['NamedEntity'],
         'slot_uri': 'dcterms:description'} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity record was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:created'} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity record was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:modified'} })


class PIIPrincipal(PrivacyStakeholder):
    """
    Schema class for a data subject — the individual to whom PII belongs. Links consent records and privacy preferences to the natural person whose data is being processed, enabling subject-centric data models.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso29100_clause': {'tag': 'iso29100_clause', 'value': '3.9'}},
         'comments': ['A PII principal may be identified directly or indirectly '
                      'through a combination of attributes',
                      'Reference: ISO/IEC 29100:2024 Clause 3.9 and 5.2.2. ISO/IEC '
                      'standards text is copyright ISO - not reproduced here.'],
         'exact_mappings': ['dpv:DataSubject'],
         'from_schema': 'https://w3id.org/lmodel/iso29100',
         'in_subset': ['privacy_framework_core'],
         'narrow_mappings': ['schema:Person']})

    privacy_preferences: Optional[list[PrivacyPreference]] = Field(default=None, description="""Privacy preferences expressed by the PII principal.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso29100_clause': {'tag': 'iso29100_clause',
                                             'value': '3.15'}},
         'domain_of': ['PIIPrincipal']} })
    consent_records: Optional[list[ConsentRecord]] = Field(default=None, description="""Consent records associated with the PII principal.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso29100_clause': {'tag': 'iso29100_clause', 'value': '3.4'}},
         'domain_of': ['PIIPrincipal']} })
    contact_information: Optional[str] = Field(default=None, description="""Contact details for the privacy stakeholder.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrivacyStakeholder']} })
    jurisdictions: Optional[list[str]] = Field(default=None, description="""Jurisdictions in which the privacy stakeholder operates.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrivacyStakeholder']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'examples': [{'value': 'iso29100:framework-acme-corp'},
                      {'value': 'iso29100:pii-controller-001'}],
         'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Should provide sufficient detail for understanding without '
                      'external reference'],
         'domain_of': ['NamedEntity'],
         'slot_uri': 'dcterms:description'} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity record was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:created'} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity record was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:modified'} })


class PIIController(PrivacyStakeholder):
    """
    Schema class for an organization or individual that determines why and how PII is processed. Captures appointed processors, legal bases relied upon, privacy policy reference, and data protection officer details. Bears ultimate accountability for privacy principle adherence.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso29100_clause': {'tag': 'iso29100_clause', 'value': '3.8'}},
         'comments': ['May appoint PII processors to process PII on its behalf while '
                      'retaining responsibility',
                      'More than one PII controller may exist for the same PII set',
                      'Reference: ISO/IEC 29100:2024 Clause 3.8 and 5.2.3. ISO/IEC '
                      'standards text is copyright ISO - not reproduced here.'],
         'exact_mappings': ['dpv:DataController'],
         'from_schema': 'https://w3id.org/lmodel/iso29100',
         'in_subset': ['privacy_framework_core'],
         'related_mappings': ['schema:Organization']})

    processing_purposes: Optional[list[str]] = Field(default=None, description="""Purposes for which the PII controller processes PII.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso29100_clause': {'tag': 'iso29100_clause', 'value': '6.3'}},
         'domain_of': ['PIIController']} })
    legal_bases: Optional[list[str]] = Field(default=None, description="""Legal bases relied upon for PII processing by this controller.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso29100_clause': {'tag': 'iso29100_clause',
                                             'value': '5.5.2'}},
         'domain_of': ['PIIController']} })
    appointed_processors: Optional[list[str]] = Field(default=None, description="""PII processors appointed by this controller.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso29100_clause': {'tag': 'iso29100_clause', 'value': '3.8'}},
         'domain_of': ['PIIController']} })
    privacy_policy_ref: Optional[str] = Field(default=None, description="""Reference to the privacy policy of this PII controller.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PIIController']} })
    data_protection_officer: Optional[str] = Field(default=None, description="""Name or contact of the data protection officer, where applicable.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PIIController']} })
    contact_information: Optional[str] = Field(default=None, description="""Contact details for the privacy stakeholder.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrivacyStakeholder']} })
    jurisdictions: Optional[list[str]] = Field(default=None, description="""Jurisdictions in which the privacy stakeholder operates.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrivacyStakeholder']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'examples': [{'value': 'iso29100:framework-acme-corp'},
                      {'value': 'iso29100:pii-controller-001'}],
         'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Should provide sufficient detail for understanding without '
                      'external reference'],
         'domain_of': ['NamedEntity'],
         'slot_uri': 'dcterms:description'} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity record was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:created'} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity record was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:modified'} })


class PIIProcessor(PrivacyStakeholder):
    """
    Schema class for an organization engaged to process PII under a PII controller's instructions. Records the instructing controller, data processing agreement reference, and any sub-processors engaged on the controller's behalf.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso29100_clause': {'tag': 'iso29100_clause',
                                             'value': '3.10'}},
         'comments': ['In some jurisdictions the PII processor is bound by a contract',
                      "{'Distinct from a third party': 'legal control of PII remains "
                      "with the original PII controller'}",
                      'Reference: ISO/IEC 29100:2024 Clause 3.10 and 5.2.4. ISO/IEC '
                      'standards text is copyright ISO - not reproduced here.'],
         'exact_mappings': ['dpv:DataProcessor'],
         'from_schema': 'https://w3id.org/lmodel/iso29100',
         'in_subset': ['privacy_framework_core']})

    instructing_controller: Optional[str] = Field(default=None, description="""The PII controller on whose behalf this processor acts.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso29100_clause': {'tag': 'iso29100_clause',
                                             'value': '3.10'}},
         'domain_of': ['PIIProcessor']} })
    processing_agreement_ref: Optional[str] = Field(default=None, description="""Reference to the data processing agreement with the controller.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso29100_clause': {'tag': 'iso29100_clause',
                                             'value': '5.5.3'}},
         'domain_of': ['PIIProcessor']} })
    sub_processors: Optional[list[str]] = Field(default=None, description="""Sub-processors engaged by this PII processor.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PIIProcessor']} })
    contact_information: Optional[str] = Field(default=None, description="""Contact details for the privacy stakeholder.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrivacyStakeholder']} })
    jurisdictions: Optional[list[str]] = Field(default=None, description="""Jurisdictions in which the privacy stakeholder operates.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrivacyStakeholder']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'examples': [{'value': 'iso29100:framework-acme-corp'},
                      {'value': 'iso29100:pii-controller-001'}],
         'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Should provide sufficient detail for understanding without '
                      'external reference'],
         'domain_of': ['NamedEntity'],
         'slot_uri': 'dcterms:description'} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity record was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:created'} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity record was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:modified'} })


class ThirdParty(PrivacyStakeholder):
    """
    Schema class for an external entity that receives PII outside the PII processor relationship — i.e., as a recipient that typically becomes a PII controller in its own right. Captures the receiving purpose and the legal basis for the transfer.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso29100_clause': {'tag': 'iso29100_clause',
                                             'value': '3.24'}},
         'comments': ['Third parties do not process PII on behalf of the original PII '
                      'controller',
                      'Upon receiving PII, a third party typically assumes controller '
                      'responsibilities',
                      'Reference: ISO/IEC 29100:2024 Clause 3.24 and 5.2.5. ISO/IEC '
                      'standards text is copyright ISO - not reproduced here.'],
         'exact_mappings': ['dpv:ThirdParty'],
         'from_schema': 'https://w3id.org/lmodel/iso29100',
         'in_subset': ['privacy_framework_core']})

    receiving_purpose: Optional[str] = Field(default=None, description="""Purpose for which the third party receives PII.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ThirdParty']} })
    transfer_basis: Optional[str] = Field(default=None, description="""Legal or contractual basis for transferring PII to this third party.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso29100_clause': {'tag': 'iso29100_clause',
                                             'value': '5.5.2'}},
         'domain_of': ['ThirdParty']} })
    contact_information: Optional[str] = Field(default=None, description="""Contact details for the privacy stakeholder.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrivacyStakeholder']} })
    jurisdictions: Optional[list[str]] = Field(default=None, description="""Jurisdictions in which the privacy stakeholder operates.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrivacyStakeholder']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'examples': [{'value': 'iso29100:framework-acme-corp'},
                      {'value': 'iso29100:pii-controller-001'}],
         'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Should provide sufficient detail for understanding without '
                      'external reference'],
         'domain_of': ['NamedEntity'],
         'slot_uri': 'dcterms:description'} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity record was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:created'} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity record was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:modified'} })


class PersonallyIdentifiableInformation(NamedEntity):
    """
    Schema class representing a data element or attribute set that can be linked back to a natural person — either directly or through combination with other attributes. Captures sensitivity classification, identifier type, pseudonymization status, retention schedule, and processing operations applicable to the data.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso29100_clause': {'tag': 'iso29100_clause', 'value': '3.7'}},
         'broad_mappings': ['dpv:PersonalData'],
         'comments': ['Encompasses direct identifiers, linkable attributes, and '
                      'combinations thereof',
                      'Sensitivity assessment should consider context and combination '
                      'of attributes',
                      'Reference: ISO/IEC 29100:2024 Clause 3.7 and 5.4. ISO/IEC '
                      'standards text is copyright ISO - not reproduced here.'],
         'from_schema': 'https://w3id.org/lmodel/iso29100',
         'in_subset': ['pii_recognition']})

    pii_category: Optional[list[str]] = Field(default=None, description="""Category or type of PII (e.g., financial, health, biometric, location).""", json_schema_extra = { "linkml_meta": {'comments': ['See Table 2 of the standard for informative examples of '
                      'attributes that can be PII'],
         'domain_of': ['PersonallyIdentifiableInformation']} })
    sensitivity_level: Optional[PIISensitivityCategory] = Field(default=None, description="""Sensitivity classification of this PII.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso29100_clause': {'tag': 'iso29100_clause',
                                             'value': '3.23'}},
         'domain_of': ['PersonallyIdentifiableInformation']} })
    identifier_type: Optional[str] = Field(default=None, description="""Type of identifier (e.g., direct identifier, indirect identifier, linkable attribute, or combination of attributes).""", json_schema_extra = { "linkml_meta": {'annotations': {'iso29100_clause': {'tag': 'iso29100_clause',
                                             'value': '5.4.2'}},
         'domain_of': ['PersonallyIdentifiableInformation']} })
    is_pseudonymized: Optional[bool] = Field(default=None, description="""Whether the PII has been pseudonymized.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso29100_clause': {'tag': 'iso29100_clause',
                                             'value': '3.22'}},
         'domain_of': ['PersonallyIdentifiableInformation']} })
    is_anonymized: Optional[bool] = Field(default=None, description="""Whether the PII has been anonymized. Anonymized data is no longer considered PII as the PII principal can no longer be identified.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso29100_clause': {'tag': 'iso29100_clause', 'value': '3.2'}},
         'domain_of': ['PersonallyIdentifiableInformation']} })
    linkability_risk: Optional[str] = Field(default=None, description="""Assessment of the risk that this data can be linked to identify a PII principal, even if not directly identifying on its own.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso29100_clause': {'tag': 'iso29100_clause',
                                             'value': '5.4.5'}},
         'domain_of': ['PersonallyIdentifiableInformation']} })
    applicable_to_principal: Optional[str] = Field(default=None, description="""Reference or description of the PII principal(s) to whom this PII relates.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PersonallyIdentifiableInformation']} })
    retention_schedule: Optional[str] = Field(default=None, description="""Schedule defining how long this PII is retained and how it is disposed.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso29100_clause': {'tag': 'iso29100_clause', 'value': '6.6'}},
         'domain_of': ['PersonallyIdentifiableInformation']} })
    processing_operations: Optional[list[PIIProcessingOperation]] = Field(default=None, description="""Types of processing operations performed on this PII.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso29100_clause': {'tag': 'iso29100_clause',
                                             'value': '3.21'}},
         'domain_of': ['PersonallyIdentifiableInformation']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'examples': [{'value': 'iso29100:framework-acme-corp'},
                      {'value': 'iso29100:pii-controller-001'}],
         'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Should provide sufficient detail for understanding without '
                      'external reference'],
         'domain_of': ['NamedEntity'],
         'slot_uri': 'dcterms:description'} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity record was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:created'} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity record was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:modified'} })


class PIIFlowScenario(NamedEntity):
    """
    A documented scenario describing the flow of PII among privacy framework actors (PII principal, PII controller, PII processor, and third party), as illustrated in Table 1 of Clause 5.3.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso29100_clause': {'tag': 'iso29100_clause', 'value': '5.3'}},
         'comments': ['Eight canonical flow scenarios are identified in Table 1 of the '
                      'standard',
                      'Reference: ISO/IEC 29100:2024 Clause 5.3 and Table 1. ISO/IEC '
                      'standards text is copyright ISO - not reproduced here.'],
         'exact_mappings': ['dpv:PersonalDataHandling'],
         'from_schema': 'https://w3id.org/lmodel/iso29100',
         'in_subset': ['privacy_framework_core']})

    scenario_label: Optional[str] = Field(default=None, description="""Label for the PII flow scenario (e.g., \"Scenario a\").""", json_schema_extra = { "linkml_meta": {'annotations': {'iso29100_clause': {'tag': 'iso29100_clause', 'value': '5.3'}},
         'domain_of': ['PIIFlowScenario']} })
    pii_principal_role: Optional[PIIFlowRole] = Field(default=None, description="""Role of the PII principal in this flow scenario.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso29100_clause': {'tag': 'iso29100_clause', 'value': '5.3'}},
         'domain_of': ['PIIFlowScenario']} })
    pii_controller_role: Optional[PIIFlowRole] = Field(default=None, description="""Role of the PII controller in this flow scenario.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso29100_clause': {'tag': 'iso29100_clause', 'value': '5.3'}},
         'domain_of': ['PIIFlowScenario']} })
    pii_processor_role: Optional[PIIFlowRole] = Field(default=None, description="""Role of the PII processor in this flow scenario.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso29100_clause': {'tag': 'iso29100_clause', 'value': '5.3'}},
         'domain_of': ['PIIFlowScenario']} })
    third_party_role: Optional[PIIFlowRole] = Field(default=None, description="""Role of the third party in this flow scenario.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso29100_clause': {'tag': 'iso29100_clause', 'value': '5.3'}},
         'domain_of': ['PIIFlowScenario']} })
    scenario_description: Optional[str] = Field(default=None, description="""Description of the PII flow scenario and when it occurs.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PIIFlowScenario']} })
    legal_control_retention: Optional[str] = Field(default=None, description="""Description of how legal control of PII is retained or transferred, relevant to distinguishing between a PII processor and a third party.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso29100_clause': {'tag': 'iso29100_clause', 'value': '5.3'}},
         'domain_of': ['PIIFlowScenario']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'examples': [{'value': 'iso29100:framework-acme-corp'},
                      {'value': 'iso29100:pii-controller-001'}],
         'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Should provide sufficient detail for understanding without '
                      'external reference'],
         'domain_of': ['NamedEntity'],
         'slot_uri': 'dcterms:description'} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity record was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:created'} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity record was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:modified'} })


class PrivacySafeguardingRequirement(NamedEntity):
    """
    Schema class for an applicable requirement that drives an organization's PII processing controls. Requirements are identified through the privacy risk management process and arise from legal/regulatory, contractual, business, or other influencing factors.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso29100_clause': {'tag': 'iso29100_clause',
                                             'value': '3.19'}},
         'comments': ['Identified through the privacy risk management process',
                      'Can range from high-level principles to specific control '
                      'mandates',
                      'Reference: ISO/IEC 29100:2024 Clause 3.19 and 5.5. ISO/IEC '
                      'standards text is copyright ISO - not reproduced here.'],
         'from_schema': 'https://w3id.org/lmodel/iso29100',
         'in_subset': ['privacy_safeguarding']})

    requirement_factor: Optional[SafeguardingRequirementFactor] = Field(default=None, description="""Category of factor driving this safeguarding requirement.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso29100_clause': {'tag': 'iso29100_clause', 'value': '5.5'}},
         'domain_of': ['PrivacySafeguardingRequirement']} })
    requirement_text: Optional[str] = Field(default=None, description="""Organization-authored statement of the safeguarding requirement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrivacySafeguardingRequirement']} })
    source_reference: Optional[str] = Field(default=None, description="""Reference to the source (e.g., law name, regulation, contract, or standard).""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrivacySafeguardingRequirement']} })
    applicable_to_actors: Optional[list[str]] = Field(default=None, description="""Privacy stakeholder roles to which this requirement applies.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrivacySafeguardingRequirement']} })
    related_controls: Optional[list[str]] = Field(default=None, description="""Privacy controls that implement or contribute to this requirement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrivacySafeguardingRequirement']} })
    priority: Optional[str] = Field(default=None, description="""Priority level for addressing this requirement or risk.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrivacySafeguardingRequirement']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'examples': [{'value': 'iso29100:framework-acme-corp'},
                      {'value': 'iso29100:pii-controller-001'}],
         'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Should provide sufficient detail for understanding without '
                      'external reference'],
         'domain_of': ['NamedEntity'],
         'slot_uri': 'dcterms:description'} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity record was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:created'} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity record was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:modified'} })


class PrivacyPolicy(NamedEntity):
    """
    Schema class for a governing document expressing an organization's intentions and commitments for PII processing. Covers both the internal policy document and any external privacy notice made available to PII principals (referred to as a notice in this framework).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso29100_clause': {'tag': 'iso29100_clause',
                                             'value': '3.14'}},
         'comments': ["Internal privacy policy expresses the organization's "
                      'commitments',
                      'External privacy policy (notice) provides information to PII '
                      'principals',
                      'Reference: ISO/IEC 29100:2024 Clause 3.14 and 5.6. ISO/IEC '
                      'standards text is copyright ISO - not reproduced here.'],
         'exact_mappings': ['schema:PrivacyPolicy', 'dpv:PrivacyNotice'],
         'from_schema': 'https://w3id.org/lmodel/iso29100',
         'in_subset': ['privacy_governance'],
         'related_mappings': ['iso27001:InformationSecurityPolicy']})

    policy_version: Optional[str] = Field(default=None, description="""Version identifier for the privacy policy.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrivacyPolicy'], 'slot_uri': 'dcterms:hasVersion'} })
    effective_date: Optional[date] = Field(default=None, description="""Date from which the privacy policy takes effect.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrivacyPolicy']} })
    policy_scope: Optional[str] = Field(default=None, description="""Scope of the privacy policy (systems, activities, or organizations covered).""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrivacyPolicy']} })
    processing_purposes_covered: Optional[list[str]] = Field(default=None, description="""Processing purposes addressed by this privacy policy.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrivacyPolicy']} })
    pii_categories_covered: Optional[list[str]] = Field(default=None, description="""Categories of PII addressed by this privacy policy.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrivacyPolicy']} })
    data_retention_statement: Optional[str] = Field(default=None, description="""Statement on how long PII is retained and how it is disposed.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso29100_clause': {'tag': 'iso29100_clause', 'value': '6.6'}},
         'domain_of': ['PrivacyPolicy']} })
    pii_principal_rights: Optional[list[str]] = Field(default=None, description="""Rights available to PII principals under this policy.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso29100_clause': {'tag': 'iso29100_clause', 'value': '6.9'}},
         'domain_of': ['PrivacyPolicy']} })
    contact_for_inquiries: Optional[str] = Field(default=None, description="""Contact information for PII-related inquiries from PII principals.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrivacyPolicy']} })
    last_review_date: Optional[date] = Field(default=None, description="""Date when the policy was last reviewed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrivacyPolicy']} })
    is_external_notice: Optional[bool] = Field(default=None, description="""Whether this is an external privacy notice (available to PII principals) rather than an internal policy document.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso29100_clause': {'tag': 'iso29100_clause', 'value': '5.6'}},
         'domain_of': ['PrivacyPolicy']} })
    applicable_principles: Optional[list[PrivacyPrinciple]] = Field(default=None, description="""Privacy principles this policy addresses.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrivacyPolicy']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'examples': [{'value': 'iso29100:framework-acme-corp'},
                      {'value': 'iso29100:pii-controller-001'}],
         'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Should provide sufficient detail for understanding without '
                      'external reference'],
         'domain_of': ['NamedEntity'],
         'slot_uri': 'dcterms:description'} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity record was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:created'} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity record was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:modified'} })


class PrivacyControl(NamedEntity):
    """
    Schema class for a protective measure that manages privacy risks within the framework. Can be organizational, physical, technical (including Privacy Enhancing Technologies), or legal-contractual in nature; linked to the principles and safeguarding requirements it addresses.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso29100_clause': {'tag': 'iso29100_clause',
                                             'value': '3.12'}},
         'comments': ['Also used as a synonym for safeguard or countermeasure',
                      'Should be identified through privacy risk assessment and '
                      'treatment',
                      "{'Privacy by design': 'controls should be integrated at the "
                      "design phase of ICT systems'}",
                      'Reference: ISO/IEC 29100:2024 Clause 3.12 and 5.7. ISO/IEC '
                      'standards text is copyright ISO - not reproduced here.'],
         'exact_mappings': ['dpv:TechnicalOrganisationalMeasure'],
         'from_schema': 'https://w3id.org/lmodel/iso29100',
         'in_subset': ['privacy_governance'],
         'related_mappings': ['iso27001:SecurityControl']})

    control_type: Optional[PrivacyControlType] = Field(default=None, description="""Category of this privacy control.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso29100_clause': {'tag': 'iso29100_clause',
                                             'value': '3.12'}},
         'domain_of': ['PrivacyControl']} })
    control_objective: Optional[str] = Field(default=None, description="""The privacy objective this control is intended to achieve.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrivacyControl']} })
    addressed_principles: Optional[list[PrivacyPrinciple]] = Field(default=None, description="""Privacy principles this control helps implement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrivacyControl']} })
    implementation_description: Optional[str] = Field(default=None, description="""Organization-authored description of how the control is implemented.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrivacyControl']} })
    responsible_actor: Optional[str] = Field(default=None, description="""Actor responsible for implementing and maintaining this control.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrivacyControl']} })
    implementation_status: Optional[str] = Field(default=None, description="""Current implementation status of the control.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrivacyControl'],
         'examples': [{'value': 'planned'},
                      {'value': 'implemented'},
                      {'value': 'not_applicable'}]} })
    effectiveness_evidence: Optional[list[str]] = Field(default=None, description="""Evidence of control effectiveness.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrivacyControl']} })
    related_safeguarding_requirements: Optional[list[str]] = Field(default=None, description="""Safeguarding requirements this control addresses.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrivacyControl']} })
    is_pet: Optional[bool] = Field(default=None, description="""Whether this control qualifies as a Privacy Enhancing Technology (PET): an ICT-based privacy control that protects privacy by minimizing, eliminating, or preventing unnecessary PII processing without reducing the intended functionality of the system.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso29100_clause': {'tag': 'iso29100_clause',
                                             'value': '3.13'}},
         'domain_of': ['PrivacyControl']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'examples': [{'value': 'iso29100:framework-acme-corp'},
                      {'value': 'iso29100:pii-controller-001'}],
         'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Should provide sufficient detail for understanding without '
                      'external reference'],
         'domain_of': ['NamedEntity'],
         'slot_uri': 'dcterms:description'} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity record was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:created'} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity record was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:modified'} })


class PrivacyRisk(NamedEntity):
    """
    Schema class representing a potential adverse outcome for PII principals from a PII processing activity. Captures the risk source, likelihood and impact assessments, inherent and residual risk levels, and links to mitigating controls and accountable risk owner.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso29100_clause': {'tag': 'iso29100_clause',
                                             'value': '3.17'}},
         'comments': ['Should be assessed in terms of likelihood and potential '
                      'consequences for PII principals',
                      'Corresponds to risk in ISO/IEC 27000 context (Annex A Table)',
                      'Reference: ISO/IEC 29100:2024 Clause 3.17 and 5.5. ISO/IEC '
                      'standards text is copyright ISO - not reproduced here.'],
         'exact_mappings': ['dpv:Risk'],
         'from_schema': 'https://w3id.org/lmodel/iso29100',
         'in_subset': ['privacy_risk_management'],
         'related_mappings': ['iso27001:Risk']})

    risk_source: Optional[str] = Field(default=None, description="""Source or origin of the privacy risk.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrivacyRisk']} })
    affected_pii_categories: Optional[list[str]] = Field(default=None, description="""Categories of PII affected by this privacy risk or breach.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrivacyRisk', 'PrivacyBreach']} })
    affected_principals_description: Optional[str] = Field(default=None, description="""Description of PII principals who could be adversely affected.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrivacyRisk']} })
    risk_likelihood: Optional[str] = Field(default=None, description="""Assessed likelihood of this privacy risk materializing.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrivacyRisk']} })
    risk_impact_description: Optional[str] = Field(default=None, description="""Description of potential adverse consequences for PII principals.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrivacyRisk']} })
    inherent_risk_level: Optional[PrivacyRiskLevel] = Field(default=None, description="""Privacy risk level before controls are applied.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrivacyRisk']} })
    residual_risk_level: Optional[PrivacyRiskLevel] = Field(default=None, description="""Privacy risk level after controls are applied.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrivacyRisk']} })
    mitigating_controls: Optional[list[str]] = Field(default=None, description="""Privacy controls that mitigate this risk.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrivacyRisk']} })
    risk_owner: Optional[str] = Field(default=None, description="""Person accountable for managing this privacy risk.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrivacyRisk']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'examples': [{'value': 'iso29100:framework-acme-corp'},
                      {'value': 'iso29100:pii-controller-001'}],
         'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Should provide sufficient detail for understanding without '
                      'external reference'],
         'domain_of': ['NamedEntity'],
         'slot_uri': 'dcterms:description'} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity record was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:created'} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity record was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:modified'} })


class PrivacyImpactAssessment(NamedEntity):
    """
    Schema class for a structured evaluation of the privacy implications of a processing activity or ICT system. Records assessment scope, identified and treated risks, accepted residual risks, stakeholder consultation records, and overall assessment outcome.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso29100_clause': {'tag': 'iso29100_clause',
                                             'value': '3.18'}},
         'comments': ['Should be conducted before implementing new or substantially '
                      'modified ICT systems',
                      "Should be framed within the organization's broader risk "
                      'management framework',
                      'Reference: ISO/IEC 29100:2024 Clause 3.18 and 5.5. ISO/IEC '
                      'standards text is copyright ISO - not reproduced here.'],
         'exact_mappings': ['dpv:PIA'],
         'from_schema': 'https://w3id.org/lmodel/iso29100',
         'in_subset': ['privacy_risk_management'],
         'related_mappings': ['iso27001:RiskAssessment']})

    assessment_scope: Optional[str] = Field(default=None, description="""Scope of the privacy impact assessment.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso29100_clause': {'tag': 'iso29100_clause',
                                             'value': '3.18'}},
         'domain_of': ['PrivacyImpactAssessment']} })
    assessment_date: Optional[date] = Field(default=None, description="""Date the assessment was conducted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrivacyImpactAssessment']} })
    assessor: Optional[str] = Field(default=None, description="""Person or team who conducted the assessment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrivacyImpactAssessment']} })
    processing_activities_assessed: Optional[list[str]] = Field(default=None, description="""PII processing activities reviewed in this assessment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrivacyImpactAssessment']} })
    risks_identified: Optional[list[str]] = Field(default=None, description="""Privacy risks identified during this assessment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrivacyImpactAssessment']} })
    risks_treated: Optional[list[str]] = Field(default=None, description="""Privacy risks for which treatment was planned or applied.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrivacyImpactAssessment']} })
    residual_risks_accepted: Optional[list[str]] = Field(default=None, description="""Privacy risks accepted as residual after treatment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrivacyImpactAssessment']} })
    assessment_outcome: Optional[str] = Field(default=None, description="""Overall outcome and conclusions of the privacy impact assessment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrivacyImpactAssessment']} })
    next_assessment_date: Optional[date] = Field(default=None, description="""Planned date for the next assessment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrivacyImpactAssessment']} })
    consultation_records: Optional[list[str]] = Field(default=None, description="""Records of stakeholder consultations conducted during the assessment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrivacyImpactAssessment']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'examples': [{'value': 'iso29100:framework-acme-corp'},
                      {'value': 'iso29100:pii-controller-001'}],
         'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Should provide sufficient detail for understanding without '
                      'external reference'],
         'domain_of': ['NamedEntity'],
         'slot_uri': 'dcterms:description'} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity record was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:created'} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity record was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:modified'} })


class PrivacyBreach(NamedEntity):
    """
    Schema class for a recorded incident in which PII was processed in a manner that violates applicable privacy safeguarding requirements. Tracks breach details, affected PII categories, notification obligations, remediation actions, and lessons learned.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso29100_clause': {'tag': 'iso29100_clause',
                                             'value': '3.11'}},
         'comments': ['Corresponds to an information security incident in ISO/IEC '
                      '27000 context (Annex A Table)',
                      'Remediation measures should be proportionate to the risks '
                      'associated with the breach',
                      'Reference: ISO/IEC 29100:2024 Clause 3.11. ISO/IEC standards '
                      'text is copyright ISO - not reproduced here.'],
         'exact_mappings': ['dpv:DataBreachRecord'],
         'from_schema': 'https://w3id.org/lmodel/iso29100',
         'in_subset': ['privacy_risk_management'],
         'related_mappings': ['iso27001:InformationSecurityIncident']})

    breach_datetime: Optional[datetime ] = Field(default=None, description="""Date and time when the privacy breach occurred.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrivacyBreach']} })
    discovery_datetime: Optional[datetime ] = Field(default=None, description="""Date and time when the privacy breach was discovered.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrivacyBreach']} })
    breach_description: Optional[str] = Field(default=None, description="""Description of the privacy breach and the violated requirements.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrivacyBreach']} })
    affected_pii_categories: Optional[list[str]] = Field(default=None, description="""Categories of PII affected by this privacy risk or breach.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrivacyRisk', 'PrivacyBreach']} })
    affected_principals_count: Optional[int] = Field(default=None, description="""Estimated number of PII principals whose PII was involved.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrivacyBreach']} })
    violated_requirements: Optional[list[str]] = Field(default=None, description="""Privacy safeguarding requirements violated by this breach.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso29100_clause': {'tag': 'iso29100_clause',
                                             'value': '3.11'}},
         'domain_of': ['PrivacyBreach']} })
    breach_severity: Optional[PrivacyRiskLevel] = Field(default=None, description="""Assessed severity of the privacy breach.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrivacyBreach']} })
    immediate_actions: Optional[list[str]] = Field(default=None, description="""Immediate actions taken to contain the breach.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrivacyBreach']} })
    notification_required: Optional[bool] = Field(default=None, description="""Whether notification to authorities or PII principals was required.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso29100_clause': {'tag': 'iso29100_clause',
                                             'value': '6.10'}},
         'domain_of': ['PrivacyBreach']} })
    notifications_made: Optional[list[str]] = Field(default=None, description="""Notifications made to authorities, PII principals, or other parties.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrivacyBreach']} })
    remediation_actions: Optional[list[str]] = Field(default=None, description="""Actions taken to remediate the breach and prevent recurrence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrivacyBreach']} })
    lessons_learned: Optional[str] = Field(default=None, description="""Lessons learned from the breach to improve privacy controls.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrivacyBreach']} })
    closure_datetime: Optional[datetime ] = Field(default=None, description="""Date and time when the breach record was closed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrivacyBreach']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'examples': [{'value': 'iso29100:framework-acme-corp'},
                      {'value': 'iso29100:pii-controller-001'}],
         'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Should provide sufficient detail for understanding without '
                      'external reference'],
         'domain_of': ['NamedEntity'],
         'slot_uri': 'dcterms:description'} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity record was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:created'} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity record was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:modified'} })


class PIIProcessingActivity(NamedEntity):
    """
    Schema class documenting a PII processing operation: its purpose, legal basis, operation types performed, categories of PII involved, responsible actors, applied controls, retention period, and any cross-border transfer safeguards.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso29100_clause': {'tag': 'iso29100_clause',
                                             'value': '3.21'}},
         'comments': ['Processing includes collection, storage, alteration, retrieval, '
                      'consultation, disclosure, anonymization, pseudonymization, '
                      'dissemination, deletion, destruction',
                      'Reference: ISO/IEC 29100:2024 Clause 3.21. ISO/IEC standards '
                      'text is copyright ISO - not reproduced here.'],
         'exact_mappings': ['dpv:PersonalDataProcess'],
         'from_schema': 'https://w3id.org/lmodel/iso29100',
         'in_subset': ['privacy_framework_core']})

    processing_purpose: Optional[str] = Field(default=None, description="""The specific, explicit, and legitimate purpose for this processing activity.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso29100_clause': {'tag': 'iso29100_clause', 'value': '6.3'}},
         'domain_of': ['PIIProcessingActivity']} })
    legal_basis: Optional[str] = Field(default=None, description="""Legal basis relied upon for this processing activity.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso29100_clause': {'tag': 'iso29100_clause',
                                             'value': '5.5.2'}},
         'domain_of': ['PIIProcessingActivity']} })
    operations_performed: Optional[list[PIIProcessingOperation]] = Field(default=None, description="""Processing operations performed in this activity.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso29100_clause': {'tag': 'iso29100_clause',
                                             'value': '3.21'}},
         'domain_of': ['PIIProcessingActivity']} })
    pii_categories_processed: Optional[list[str]] = Field(default=None, description="""Categories of PII processed in this activity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PIIProcessingActivity']} })
    sensitivity_levels_involved: Optional[list[PIISensitivityCategory]] = Field(default=None, description="""Sensitivity levels of PII processed in this activity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PIIProcessingActivity']} })
    controller_ref: Optional[str] = Field(default=None, description="""PII controller responsible for this processing activity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PIIProcessingActivity']} })
    processor_ref: Optional[str] = Field(default=None, description="""PII processor performing this processing activity, if applicable.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PIIProcessingActivity']} })
    data_flows: Optional[list[str]] = Field(default=None, description="""PII flow scenarios applicable to this processing activity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PIIProcessingActivity']} })
    retention_period: Optional[str] = Field(default=None, description="""Retention period for PII processed in this activity.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso29100_clause': {'tag': 'iso29100_clause', 'value': '6.6'}},
         'comments': ['Use ISO 8601 duration notation such as P1Y or P90D'],
         'domain_of': ['PIIProcessingActivity']} })
    privacy_controls_applied: Optional[list[str]] = Field(default=None, description="""Privacy controls applied to this processing activity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PIIProcessingActivity']} })
    cross_border_transfer: Optional[bool] = Field(default=None, description="""Whether this activity involves cross-border transfer of PII.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso29100_clause': {'tag': 'iso29100_clause', 'value': '6.6'}},
         'domain_of': ['PIIProcessingActivity']} })
    transfer_safeguards: Optional[list[str]] = Field(default=None, description="""Safeguards in place for cross-border PII transfers.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso29100_clause': {'tag': 'iso29100_clause', 'value': '6.6'}},
         'domain_of': ['PIIProcessingActivity']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'examples': [{'value': 'iso29100:framework-acme-corp'},
                      {'value': 'iso29100:pii-controller-001'}],
         'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Should provide sufficient detail for understanding without '
                      'external reference'],
         'domain_of': ['NamedEntity'],
         'slot_uri': 'dcterms:description'} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity record was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:created'} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity record was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:modified'} })


class PrivacyPrincipleImplementation(NamedEntity):
    """
    Documentation of how a specific privacy principle from Clause 6 has been implemented within the organization's privacy framework, including measures taken and evidence of adherence.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso29100_clause': {'tag': 'iso29100_clause', 'value': '6'}},
         'comments': ['One implementation record per principle per organization or ICT '
                      'system scope',
                      'Reference: ISO/IEC 29100:2024 Clause 6. ISO/IEC standards text '
                      'is copyright ISO - not reproduced here.'],
         'from_schema': 'https://w3id.org/lmodel/iso29100',
         'in_subset': ['privacy_principles']})

    principle: PrivacyPrinciple = Field(default=..., description="""The privacy principle being implemented.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso29100_clause': {'tag': 'iso29100_clause', 'value': '6'}},
         'domain_of': ['PrivacyPrincipleImplementation']} })
    implementation_measures: Optional[list[str]] = Field(default=None, description="""Measures taken to implement this privacy principle.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrivacyPrincipleImplementation']} })
    applicable_controls_ref: Optional[list[str]] = Field(default=None, description="""Privacy controls that contribute to implementing this principle.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrivacyPrincipleImplementation']} })
    evidence_of_adherence: Optional[list[str]] = Field(default=None, description="""Evidence demonstrating adherence to this principle.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrivacyPrincipleImplementation']} })
    gaps_identified: Optional[list[str]] = Field(default=None, description="""Identified gaps in the implementation of this principle.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrivacyPrincipleImplementation']} })
    improvement_actions: Optional[list[str]] = Field(default=None, description="""Actions planned to address identified implementation gaps.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrivacyPrincipleImplementation']} })
    last_assessed_date: Optional[date] = Field(default=None, description="""Date when adherence to this principle was last assessed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrivacyPrincipleImplementation']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'examples': [{'value': 'iso29100:framework-acme-corp'},
                      {'value': 'iso29100:pii-controller-001'}],
         'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Should provide sufficient detail for understanding without '
                      'external reference'],
         'domain_of': ['NamedEntity'],
         'slot_uri': 'dcterms:description'} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity record was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:created'} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity record was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:modified'} })


class ConsentRecord(NamedEntity):
    """
    Schema class documenting a PII principal's agreement to processing of their PII for stated purposes. Records the consent mechanism used, scope, current status, and withdrawal date — supporting auditability of the consent and choice privacy principle.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso29100_clause': {'tag': 'iso29100_clause', 'value': '3.4'}},
         'comments': ['Consent must be freely given, specific, and informed',
                      'Opt-in required for sensitive PII unless applicable law permits '
                      'otherwise',
                      'Withdrawal of consent must be easily exercisable and free of '
                      'charge',
                      'Reference: ISO/IEC 29100:2024 Clause 3.4 and 6.2. ISO/IEC '
                      'standards text is copyright ISO - not reproduced here.'],
         'exact_mappings': ['dpv:InformedConsent'],
         'from_schema': 'https://w3id.org/lmodel/iso29100',
         'in_subset': ['privacy_framework_core']})

    principal_ref: Optional[str] = Field(default=None, description="""Reference to the PII principal associated with this consent record or privacy preference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ConsentRecord', 'PrivacyPreference']} })
    consent_date: Optional[datetime ] = Field(default=None, description="""Date and time when consent was given.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso29100_clause': {'tag': 'iso29100_clause', 'value': '3.4'}},
         'domain_of': ['ConsentRecord']} })
    consent_mechanism: Optional[ConsentMechanism] = Field(default=None, description="""Mechanism by which consent was obtained.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso29100_clause': {'tag': 'iso29100_clause', 'value': '3.6'}},
         'domain_of': ['ConsentRecord']} })
    processing_purposes_consented: Optional[list[str]] = Field(default=None, description="""Processing purposes for which consent was given.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ConsentRecord']} })
    pii_categories_consented: Optional[list[str]] = Field(default=None, description="""Categories of PII for which consent was given.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ConsentRecord']} })
    withdrawal_date: Optional[datetime ] = Field(default=None, description="""Date and time when consent was withdrawn, if applicable.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso29100_clause': {'tag': 'iso29100_clause', 'value': '6.2'}},
         'domain_of': ['ConsentRecord']} })
    consent_status: Optional[str] = Field(default=None, description="""Current status of the consent.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ConsentRecord'],
         'examples': [{'value': 'active'},
                      {'value': 'withdrawn'},
                      {'value': 'expired'}]} })
    consent_evidence_ref: Optional[str] = Field(default=None, description="""Reference to evidence of consent (e.g., record identifier or URL).""", json_schema_extra = { "linkml_meta": {'domain_of': ['ConsentRecord']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'examples': [{'value': 'iso29100:framework-acme-corp'},
                      {'value': 'iso29100:pii-controller-001'}],
         'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Should provide sufficient detail for understanding without '
                      'external reference'],
         'domain_of': ['NamedEntity'],
         'slot_uri': 'dcterms:description'} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity record was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:created'} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity record was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:modified'} })


class PrivacyPreference(NamedEntity):
    """
    Schema class capturing a PII principal's processing choices for a particular purpose scope: preferences for anonymity or pseudonymity, restrictions on specific processing operations, and restrictions on disclosure to named or categorized parties.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso29100_clause': {'tag': 'iso29100_clause',
                                             'value': '3.15'}},
         'comments': ['ICT systems should offer meaningful choices where technically '
                      'feasible',
                      'Preferences may include anonymity, pseudonymity, or restriction '
                      'of specific operations',
                      'Reference: ISO/IEC 29100:2024 Clause 3.15 and 5.5.5. ISO/IEC '
                      'standards text is copyright ISO - not reproduced here.'],
         'from_schema': 'https://w3id.org/lmodel/iso29100',
         'in_subset': ['privacy_framework_core']})

    principal_ref: Optional[str] = Field(default=None, description="""Reference to the PII principal associated with this consent record or privacy preference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ConsentRecord', 'PrivacyPreference']} })
    preference_scope: Optional[str] = Field(default=None, description="""The processing activities or purposes to which these preferences apply.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrivacyPreference']} })
    anonymity_preference: Optional[bool] = Field(default=None, description="""Whether the PII principal prefers anonymous processing where possible.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso29100_clause': {'tag': 'iso29100_clause', 'value': '3.1'}},
         'domain_of': ['PrivacyPreference']} })
    pseudonymity_preference: Optional[bool] = Field(default=None, description="""Whether the PII principal prefers pseudonymous processing where possible.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso29100_clause': {'tag': 'iso29100_clause',
                                             'value': '3.22'}},
         'domain_of': ['PrivacyPreference']} })
    processing_restriction_preferences: Optional[list[PIIProcessingOperation]] = Field(default=None, description="""Specific processing operations the PII principal wishes to restrict.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrivacyPreference']} })
    disclosure_restriction_preferences: Optional[list[str]] = Field(default=None, description="""Restrictions on disclosing PII to specific parties or categories of parties.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrivacyPreference']} })
    preference_recorded_date: Optional[date] = Field(default=None, description="""Date when these privacy preferences were recorded.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrivacyPreference']} })
    id: str = Field(default=..., description="""Unique identifier for this entity instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'],
         'examples': [{'value': 'iso29100:framework-acme-corp'},
                      {'value': 'iso29100:pii-controller-001'}],
         'slot_uri': 'dcterms:identifier'} })
    name: str = Field(default=..., description="""Human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""Detailed description of the entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Should provide sufficient detail for understanding without '
                      'external reference'],
         'domain_of': ['NamedEntity'],
         'slot_uri': 'dcterms:description'} })
    created_date: Optional[date] = Field(default=None, description="""Date when the entity record was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:created'} })
    modified_date: Optional[date] = Field(default=None, description="""Date when the entity record was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedEntity'], 'slot_uri': 'dcterms:modified'} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
NamedEntity.model_rebuild()
PrivacyFramework.model_rebuild()
PrivacyStakeholder.model_rebuild()
PIIPrincipal.model_rebuild()
PIIController.model_rebuild()
PIIProcessor.model_rebuild()
ThirdParty.model_rebuild()
PersonallyIdentifiableInformation.model_rebuild()
PIIFlowScenario.model_rebuild()
PrivacySafeguardingRequirement.model_rebuild()
PrivacyPolicy.model_rebuild()
PrivacyControl.model_rebuild()
PrivacyRisk.model_rebuild()
PrivacyImpactAssessment.model_rebuild()
PrivacyBreach.model_rebuild()
PIIProcessingActivity.model_rebuild()
PrivacyPrincipleImplementation.model_rebuild()
ConsentRecord.model_rebuild()
PrivacyPreference.model_rebuild()
