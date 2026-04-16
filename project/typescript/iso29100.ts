export type NamedEntityId = string;
export type PrivacyFrameworkId = string;
export type PrivacyStakeholderId = string;
export type PIIPrincipalId = string;
export type PIIControllerId = string;
export type PIIProcessorId = string;
export type ThirdPartyId = string;
export type PersonallyIdentifiableInformationId = string;
export type PIIFlowScenarioId = string;
export type PrivacySafeguardingRequirementId = string;
export type PrivacyPolicyId = string;
export type PrivacyControlId = string;
export type PrivacyRiskId = string;
export type PrivacyImpactAssessmentId = string;
export type PrivacyBreachId = string;
export type PIIProcessingActivityId = string;
export type PrivacyPrincipleImplementationId = string;
export type ConsentRecordId = string;
export type PrivacyPreferenceId = string;
/**
* The eleven privacy principles defined in ISO/IEC 29100:2024 Clause 6 that govern the processing of PII in ICT systems.
*/
export enum PrivacyPrinciple {
    
    /** Schema value for privacy principle 1 (Clause 6.2): the organization gives PII principals meaningful choice over processing of their PII, manages opt-in consent mechanisms, and provides readily accessible means to withdraw consent. */
    consent_and_choice = "consent_and_choice",
    /** Schema value for privacy principle 2 (Clause 6.3): the organization ensures each processing purpose is lawful, relies on a valid legal basis, and is communicated to PII principals prior to or at the time of collection. */
    purpose_legitimacy_and_specification = "purpose_legitimacy_and_specification",
    /** Schema value for privacy principle 3 (Clause 6.4): the organization limits PII collection to what is lawful and strictly necessary to fulfil the stated processing purposes. */
    collection_limitation = "collection_limitation",
    /** Schema value for privacy principle 4 (Clause 6.5): the organization designs processing procedures and ICT systems to minimize the volume of PII handled and the number of parties with access to it. */
    data_minimization = "data_minimization",
    /** Schema value for privacy principle 5 (Clause 6.6): the organization limits use, retention, and disclosure of PII to the minimum needed for legitimate purposes, and securely disposes of PII once those purposes have been fulfilled. */
    use_retention_and_disclosure_limitation = "use_retention_and_disclosure_limitation",
    /** Schema value for privacy principle 6 (Clause 6.7): the organization ensures PII is accurate, complete, current, and fit for purpose, and establishes procedures for verification, correction, and ongoing quality control of processed PII. */
    accuracy_and_quality = "accuracy_and_quality",
    /** Schema value for privacy principle 7 (Clause 6.8): the organization provides PII principals with clear, accessible information about its PII processing policies and practices, and notifies them of material changes to those policies. */
    openness_transparency_and_notice = "openness_transparency_and_notice",
    /** Schema value for privacy principle 8 (Clause 6.9): the organization gives PII principals the ability to access and review their PII and to challenge its accuracy and completeness, subject to applicable law. */
    individual_participation_and_access = "individual_participation_and_access",
    /** Schema value for privacy principle 9 (Clause 6.10): the organization documents and communicates its privacy obligations, ensures equivalent protection when transferring PII to third parties, and maintains internal complaint-handling and redress procedures. */
    accountability = "accountability",
    /** Schema value for privacy principle 10 (Clause 6.11): the organization applies appropriate security controls across operational, functional, and strategic levels to protect PII against unauthorized access, loss, or misuse throughout its full lifecycle. */
    information_security = "information_security",
    /** Schema value for privacy principle 11 (Clause 6.12): the organization verifies and demonstrates compliance with data protection and privacy requirements through audits, independent internal controls, and ongoing privacy risk assessments. */
    privacy_compliance = "privacy_compliance",
};
/**
* The role played by an actor in a specific PII flow scenario, as described in Table 1 of ISO/IEC 29100:2024 Clause 5.3.
*/
export enum PIIFlowRole {
    
    /** Actor that provides PII to another party in this flow scenario. */
    pii_provider = "pii_provider",
    /** Actor that receives PII from another party in this flow scenario. */
    pii_recipient = "pii_recipient",
    /** Actor not directly involved in this specific PII flow scenario. */
    not_involved = "not_involved",
};
/**
* Categories of operations that can be performed on PII, as referenced in the definition of processing of PII (Clause 3.21).
*/
export enum PIIProcessingOperation {
    
    /** Gathering or acquiring PII from PII principals or other sources. */
    collection = "collection",
    /** Storing PII in a persistent manner in ICT systems or other media. */
    storage = "storage",
    /** Modifying or updating existing PII. */
    alteration = "alteration",
    /** Accessing or fetching stored PII for use. */
    retrieval = "retrieval",
    /** Reviewing or examining PII without necessarily extracting it. */
    consultation = "consultation",
    /** Making PII available to other parties or making it accessible. */
    disclosure = "disclosure",
    /** Irreversibly altering PII such that the PII principal can no longer be identified directly or indirectly. */
    anonymization = "anonymization",
    /** Replacing identifying information in PII with an alias, retaining linkability while restricting direct identification. */
    pseudonymization = "pseudonymization",
    /** Widely distributing or publishing PII to multiple recipients. */
    dissemination = "dissemination",
    /** Removing PII such that it is no longer accessible or usable. */
    deletion = "deletion",
    /** Permanently and irrecoverably eliminating PII and its carriers. */
    destruction = "destruction",
};
/**
* Categories of factors that influence an organization's privacy safeguarding requirements, as described in Clause 5.5 and Figure 1.
*/
export enum SafeguardingRequirementFactor {
    
    /** Safeguarding requirements arising from applicable laws (international, national, and local), regulations, judicial decisions, and negotiated labour or work-council agreements. */
    legal_and_regulatory = "legal_and_regulatory",
    /** Safeguarding requirements set out in data processing agreements, company policies, and binding corporate rules agreed between PII controllers, processors, and other parties. */
    contractual = "contractual",
    /** Safeguarding requirements driven by the application's characteristics, industry guidelines, codes of conduct, or standards voluntarily adopted by the organization as part of its business model. */
    business = "business",
    /** Safeguarding requirements arising from PII principal privacy preferences, internal control frameworks, or technical standards voluntarily adopted by the organization. */
    other = "other",
};
/**
* Categories of PII based on sensitivity, distinguishing standard PII from sensitive PII as defined in Clause 3.23.
*/
export enum PIISensitivityCategory {
    
    /** PII that does not meet the threshold for sensitive PII but still requires appropriate privacy protection measures. */
    standard = "standard",
    /** PII warranting heightened protection due to its potential for significant adverse impact on the individual, or because applicable law classifies it as a special category. Typical examples include health, biometric, financial, racial, religious, political, and sexual orientation data. Processing may require opt-in consent or specific legal authorization. */
    sensitive = "sensitive",
};
/**
* The mechanism by which a PII principal provides or withholds consent for PII processing, as referenced in Clauses 3.6 and 6.2.
*/
export enum ConsentMechanism {
    
    /** The PII principal must take an explicit action to express prior consent for their PII to be processed for a particular purpose. */
    opt_in = "opt_in",
    /** The PII principal must take a separate action to withhold or withdraw consent; processing is presumed permitted unless that action is taken. */
    opt_out = "opt_out",
    /** Consent implied by some action of the PII principal, such as placing an order or using a service, where applicable law permits. */
    implied = "implied",
};
/**
* Qualitative assessment of privacy risk level based on likelihood and potential adverse consequences for PII principals.
*/
export enum PrivacyRiskLevel {
    
    /** Limited potential adverse consequences for PII principals. */
    low = "low",
    /** Moderate risk requiring management attention and planned controls. */
    medium = "medium",
    /** Significant risk with potentially serious consequences for PII principals. */
    high = "high",
    /** Severe risk with potentially catastrophic or irreversible consequences for PII principals requiring immediate treatment. */
    very_high = "very_high",
};
/**
* Categories of privacy controls that treat privacy risks by reducing their likelihood or consequences, as noted in Clause 3.12 Note 1.
*/
export enum PrivacyControlType {
    
    /** Policies, procedures, guidelines, management practices, or organizational structures used as privacy controls. */
    organizational = "organizational",
    /** Physical measures protecting PII and PII processing infrastructure. */
    physical = "physical",
    /** ICT measures, products, or services that protect privacy, including privacy enhancing technologies (PETs). */
    technical = "technical",
    /** Legal contracts, binding corporate rules, or data processing agreements implementing privacy safeguards. */
    legal_contractual = "legal_contractual",
};


/**
 * Abstract base class for all entities with a unique identifier, name, and description. Provides common identification and documentation slots.
 */
export interface NamedEntity {
    /** Unique identifier for this entity instance. */
    id: string,
    /** Human-readable name or title. */
    name: string,
    /** Detailed description of the entity. */
    description?: string,
    /** Date when the entity record was created. */
    created_date?: date,
    /** Date when the entity record was last modified. */
    modified_date?: date,
}


/**
 * Top-level container representing an organization's privacy framework for protecting PII within ICT systems.
 */
export interface PrivacyFramework extends NamedEntity {
    /** Name of the organization operating the privacy framework. */
    organization_name?: string,
    /** Description of the ICT system(s) within the scope of the privacy framework. */
    ict_system_description?: string,
    /** Legal jurisdictions whose privacy laws apply to the organization. */
    applicable_jurisdictions?: string[],
    /** PII controllers operating within this privacy framework. */
    pii_controllers?: PIIControllerId[],
    /** PII processors engaged within this privacy framework. */
    pii_processors?: PIIProcessorId[],
    /** Third parties that may receive PII within this framework. */
    third_parties?: ThirdPartyId[],
    /** Description of the categories of PII principals whose PII is processed. */
    pii_principals_description?: string,
    /** The organization's privacy policy governing PII processing. */
    privacy_policy?: PrivacyPolicyId,
    /** Privacy controls implemented within the framework. */
    privacy_controls?: PrivacyControlId[],
    /** Privacy safeguarding requirements applicable to the organization. */
    safeguarding_requirements?: PrivacySafeguardingRequirementId[],
    /** Privacy risks identified within the framework scope. */
    privacy_risks?: PrivacyRiskId[],
    /** Privacy impact assessments conducted under this framework. */
    privacy_impact_assessments?: PrivacyImpactAssessmentId[],
    /** Privacy breaches recorded within the framework. */
    privacy_breaches?: PrivacyBreachId[],
    /** PII processing activities within the framework scope. */
    pii_processing_activities?: PIIProcessingActivityId[],
    /** Implementation records for each of the eleven privacy principles. */
    principle_implementations?: PrivacyPrincipleImplementationId[],
}


/**
 * Schema base class for the four actor types recognized by the privacy framework: PII principals, PII controllers, PII processors, and third parties. Provides shared contact and jurisdictional attributes common to all stakeholder roles.
 */
export interface PrivacyStakeholder extends NamedEntity {
    /** Contact details for the privacy stakeholder. */
    contact_information?: string,
    /** Jurisdictions in which the privacy stakeholder operates. */
    jurisdictions?: string[],
}


/**
 * Schema class for a data subject — the individual to whom PII belongs. Links consent records and privacy preferences to the natural person whose data is being processed, enabling subject-centric data models.
 */
export interface PIIPrincipal extends PrivacyStakeholder {
    /** Privacy preferences expressed by the PII principal. */
    privacy_preferences?: PrivacyPreferenceId[],
    /** Consent records associated with the PII principal. */
    consent_records?: ConsentRecord[],
}


/**
 * Schema class for an organization or individual that determines why and how PII is processed. Captures appointed processors, legal bases relied upon, privacy policy reference, and data protection officer details. Bears ultimate accountability for privacy principle adherence.
 */
export interface PIIController extends PrivacyStakeholder {
    /** Purposes for which the PII controller processes PII. */
    processing_purposes?: string[],
    /** Legal bases relied upon for PII processing by this controller. */
    legal_bases?: string[],
    /** PII processors appointed by this controller. */
    appointed_processors?: PIIProcessorId[],
    /** Reference to the privacy policy of this PII controller. */
    privacy_policy_ref?: PrivacyPolicyId,
    /** Name or contact of the data protection officer, where applicable. */
    data_protection_officer?: string,
}


/**
 * Schema class for an organization engaged to process PII under a PII controller's instructions. Records the instructing controller, data processing agreement reference, and any sub-processors engaged on the controller's behalf.
 */
export interface PIIProcessor extends PrivacyStakeholder {
    /** The PII controller on whose behalf this processor acts. */
    instructing_controller?: PIIControllerId,
    /** Reference to the data processing agreement with the controller. */
    processing_agreement_ref?: string,
    /** Sub-processors engaged by this PII processor. */
    sub_processors?: PIIProcessorId[],
}


/**
 * Schema class for an external entity that receives PII outside the PII processor relationship — i.e., as a recipient that typically becomes a PII controller in its own right. Captures the receiving purpose and the legal basis for the transfer.
 */
export interface ThirdParty extends PrivacyStakeholder {
    /** Purpose for which the third party receives PII. */
    receiving_purpose?: string,
    /** Legal or contractual basis for transferring PII to this third party. */
    transfer_basis?: string,
}


/**
 * Schema class representing a data element or attribute set that can be linked back to a natural person — either directly or through combination with other attributes. Captures sensitivity classification, identifier type, pseudonymization status, retention schedule, and processing operations applicable to the data.
 */
export interface PersonallyIdentifiableInformation extends NamedEntity {
    /** Category or type of PII (e.g., financial, health, biometric, location). */
    pii_category?: string[],
    /** Sensitivity classification of this PII. */
    sensitivity_level?: string,
    /** Type of identifier (e.g., direct identifier, indirect identifier, linkable attribute, or combination of attributes). */
    identifier_type?: string,
    /** Whether the PII has been pseudonymized. */
    is_pseudonymized?: boolean,
    /** Whether the PII has been anonymized. Anonymized data is no longer considered PII as the PII principal can no longer be identified. */
    is_anonymized?: boolean,
    /** Assessment of the risk that this data can be linked to identify a PII principal, even if not directly identifying on its own. */
    linkability_risk?: string,
    /** Reference or description of the PII principal(s) to whom this PII relates. */
    applicable_to_principal?: string,
    /** Schedule defining how long this PII is retained and how it is disposed. */
    retention_schedule?: string,
    /** Types of processing operations performed on this PII. */
    processing_operations?: string,
}


/**
 * A documented scenario describing the flow of PII among privacy framework actors (PII principal, PII controller, PII processor, and third party), as illustrated in Table 1 of Clause 5.3.
 */
export interface PIIFlowScenario extends NamedEntity {
    /** Label for the PII flow scenario (e.g., "Scenario a"). */
    scenario_label?: string,
    /** Role of the PII principal in this flow scenario. */
    pii_principal_role?: string,
    /** Role of the PII controller in this flow scenario. */
    pii_controller_role?: string,
    /** Role of the PII processor in this flow scenario. */
    pii_processor_role?: string,
    /** Role of the third party in this flow scenario. */
    third_party_role?: string,
    /** Description of the PII flow scenario and when it occurs. */
    scenario_description?: string,
    /** Description of how legal control of PII is retained or transferred, relevant to distinguishing between a PII processor and a third party. */
    legal_control_retention?: string,
}


/**
 * Schema class for an applicable requirement that drives an organization's PII processing controls. Requirements are identified through the privacy risk management process and arise from legal/regulatory, contractual, business, or other influencing factors.
 */
export interface PrivacySafeguardingRequirement extends NamedEntity {
    /** Category of factor driving this safeguarding requirement. */
    requirement_factor?: string,
    /** Organization-authored statement of the safeguarding requirement. */
    requirement_text?: string,
    /** Reference to the source (e.g., law name, regulation, contract, or standard). */
    source_reference?: string,
    /** Privacy stakeholder roles to which this requirement applies. */
    applicable_to_actors?: string[],
    /** Privacy controls that implement or contribute to this requirement. */
    related_controls?: PrivacyControlId[],
    /** Priority level for addressing this requirement or risk. */
    priority?: string,
}


/**
 * Schema class for a governing document expressing an organization's intentions and commitments for PII processing. Covers both the internal policy document and any external privacy notice made available to PII principals (referred to as a notice in this framework).
 */
export interface PrivacyPolicy extends NamedEntity {
    /** Version identifier for the privacy policy. */
    policy_version?: string,
    /** Date from which the privacy policy takes effect. */
    effective_date?: date,
    /** Scope of the privacy policy (systems, activities, or organizations covered). */
    policy_scope?: string,
    /** Processing purposes addressed by this privacy policy. */
    processing_purposes_covered?: string[],
    /** Categories of PII addressed by this privacy policy. */
    pii_categories_covered?: string[],
    /** Statement on how long PII is retained and how it is disposed. */
    data_retention_statement?: string,
    /** Rights available to PII principals under this policy. */
    pii_principal_rights?: string[],
    /** Contact information for PII-related inquiries from PII principals. */
    contact_for_inquiries?: string,
    /** Date when the policy was last reviewed. */
    last_review_date?: date,
    /** Whether this is an external privacy notice (available to PII principals) rather than an internal policy document. */
    is_external_notice?: boolean,
    /** Privacy principles this policy addresses. */
    applicable_principles?: string,
}


/**
 * Schema class for a protective measure that manages privacy risks within the framework. Can be organizational, physical, technical (including Privacy Enhancing Technologies), or legal-contractual in nature; linked to the principles and safeguarding requirements it addresses.
 */
export interface PrivacyControl extends NamedEntity {
    /** Category of this privacy control. */
    control_type?: string,
    /** The privacy objective this control is intended to achieve. */
    control_objective?: string,
    /** Privacy principles this control helps implement. */
    addressed_principles?: string,
    /** Organization-authored description of how the control is implemented. */
    implementation_description?: string,
    /** Actor responsible for implementing and maintaining this control. */
    responsible_actor?: string,
    /** Current implementation status of the control. */
    implementation_status?: string,
    /** Evidence of control effectiveness. */
    effectiveness_evidence?: string[],
    /** Safeguarding requirements this control addresses. */
    related_safeguarding_requirements?: PrivacySafeguardingRequirementId[],
    /** Whether this control qualifies as a Privacy Enhancing Technology (PET): an ICT-based privacy control that protects privacy by minimizing, eliminating, or preventing unnecessary PII processing without reducing the intended functionality of the system. */
    is_pet?: boolean,
}


/**
 * Schema class representing a potential adverse outcome for PII principals from a PII processing activity. Captures the risk source, likelihood and impact assessments, inherent and residual risk levels, and links to mitigating controls and accountable risk owner.
 */
export interface PrivacyRisk extends NamedEntity {
    /** Source or origin of the privacy risk. */
    risk_source?: string,
    /** Categories of PII affected by this privacy risk or breach. */
    affected_pii_categories?: string[],
    /** Description of PII principals who could be adversely affected. */
    affected_principals_description?: string,
    /** Assessed likelihood of this privacy risk materializing. */
    risk_likelihood?: string,
    /** Description of potential adverse consequences for PII principals. */
    risk_impact_description?: string,
    /** Privacy risk level before controls are applied. */
    inherent_risk_level?: string,
    /** Privacy risk level after controls are applied. */
    residual_risk_level?: string,
    /** Privacy controls that mitigate this risk. */
    mitigating_controls?: PrivacyControlId[],
    /** Person accountable for managing this privacy risk. */
    risk_owner?: string,
}


/**
 * Schema class for a structured evaluation of the privacy implications of a processing activity or ICT system. Records assessment scope, identified and treated risks, accepted residual risks, stakeholder consultation records, and overall assessment outcome.
 */
export interface PrivacyImpactAssessment extends NamedEntity {
    /** Scope of the privacy impact assessment. */
    assessment_scope?: string,
    /** Date the assessment was conducted. */
    assessment_date?: date,
    /** Person or team who conducted the assessment. */
    assessor?: string,
    /** PII processing activities reviewed in this assessment. */
    processing_activities_assessed?: PIIProcessingActivityId[],
    /** Privacy risks identified during this assessment. */
    risks_identified?: PrivacyRiskId[],
    /** Privacy risks for which treatment was planned or applied. */
    risks_treated?: PrivacyRiskId[],
    /** Privacy risks accepted as residual after treatment. */
    residual_risks_accepted?: PrivacyRiskId[],
    /** Overall outcome and conclusions of the privacy impact assessment. */
    assessment_outcome?: string,
    /** Planned date for the next assessment. */
    next_assessment_date?: date,
    /** Records of stakeholder consultations conducted during the assessment. */
    consultation_records?: string[],
}


/**
 * Schema class for a recorded incident in which PII was processed in a manner that violates applicable privacy safeguarding requirements. Tracks breach details, affected PII categories, notification obligations, remediation actions, and lessons learned.
 */
export interface PrivacyBreach extends NamedEntity {
    /** Date and time when the privacy breach occurred. */
    breach_datetime?: string,
    /** Date and time when the privacy breach was discovered. */
    discovery_datetime?: string,
    /** Description of the privacy breach and the violated requirements. */
    breach_description?: string,
    /** Categories of PII affected by this privacy risk or breach. */
    affected_pii_categories?: string[],
    /** Estimated number of PII principals whose PII was involved. */
    affected_principals_count?: number,
    /** Privacy safeguarding requirements violated by this breach. */
    violated_requirements?: PrivacySafeguardingRequirementId[],
    /** Assessed severity of the privacy breach. */
    breach_severity?: string,
    /** Immediate actions taken to contain the breach. */
    immediate_actions?: string[],
    /** Whether notification to authorities or PII principals was required. */
    notification_required?: boolean,
    /** Notifications made to authorities, PII principals, or other parties. */
    notifications_made?: string[],
    /** Actions taken to remediate the breach and prevent recurrence. */
    remediation_actions?: string[],
    /** Lessons learned from the breach to improve privacy controls. */
    lessons_learned?: string,
    /** Date and time when the breach record was closed. */
    closure_datetime?: string,
}


/**
 * Schema class documenting a PII processing operation: its purpose, legal basis, operation types performed, categories of PII involved, responsible actors, applied controls, retention period, and any cross-border transfer safeguards.
 */
export interface PIIProcessingActivity extends NamedEntity {
    /** The specific, explicit, and legitimate purpose for this processing activity. */
    processing_purpose?: string,
    /** Legal basis relied upon for this processing activity. */
    legal_basis?: string,
    /** Processing operations performed in this activity. */
    operations_performed?: string,
    /** Categories of PII processed in this activity. */
    pii_categories_processed?: string[],
    /** Sensitivity levels of PII processed in this activity. */
    sensitivity_levels_involved?: string,
    /** PII controller responsible for this processing activity. */
    controller_ref?: PIIControllerId,
    /** PII processor performing this processing activity, if applicable. */
    processor_ref?: PIIProcessorId,
    /** PII flow scenarios applicable to this processing activity. */
    data_flows?: PIIFlowScenarioId[],
    /** Retention period for PII processed in this activity. */
    retention_period?: string,
    /** Privacy controls applied to this processing activity. */
    privacy_controls_applied?: PrivacyControlId[],
    /** Whether this activity involves cross-border transfer of PII. */
    cross_border_transfer?: boolean,
    /** Safeguards in place for cross-border PII transfers. */
    transfer_safeguards?: string[],
}


/**
 * Documentation of how a specific privacy principle from Clause 6 has been implemented within the organization's privacy framework, including measures taken and evidence of adherence.
 */
export interface PrivacyPrincipleImplementation extends NamedEntity {
    /** The privacy principle being implemented. */
    principle: string,
    /** Measures taken to implement this privacy principle. */
    implementation_measures?: string[],
    /** Privacy controls that contribute to implementing this principle. */
    applicable_controls_ref?: PrivacyControlId[],
    /** Evidence demonstrating adherence to this principle. */
    evidence_of_adherence?: string[],
    /** Identified gaps in the implementation of this principle. */
    gaps_identified?: string[],
    /** Actions planned to address identified implementation gaps. */
    improvement_actions?: string[],
    /** Date when adherence to this principle was last assessed. */
    last_assessed_date?: date,
}


/**
 * Schema class documenting a PII principal's agreement to processing of their PII for stated purposes. Records the consent mechanism used, scope, current status, and withdrawal date — supporting auditability of the consent and choice privacy principle.
 */
export interface ConsentRecord extends NamedEntity {
    /** Reference to the PII principal associated with this consent record or privacy preference. */
    principal_ref?: string,
    /** Date and time when consent was given. */
    consent_date?: string,
    /** Mechanism by which consent was obtained. */
    consent_mechanism?: string,
    /** Processing purposes for which consent was given. */
    processing_purposes_consented?: string[],
    /** Categories of PII for which consent was given. */
    pii_categories_consented?: string[],
    /** Date and time when consent was withdrawn, if applicable. */
    withdrawal_date?: string,
    /** Current status of the consent. */
    consent_status?: string,
    /** Reference to evidence of consent (e.g., record identifier or URL). */
    consent_evidence_ref?: string,
}


/**
 * Schema class capturing a PII principal's processing choices for a particular purpose scope: preferences for anonymity or pseudonymity, restrictions on specific processing operations, and restrictions on disclosure to named or categorized parties.
 */
export interface PrivacyPreference extends NamedEntity {
    /** Reference to the PII principal associated with this consent record or privacy preference. */
    principal_ref?: string,
    /** The processing activities or purposes to which these preferences apply. */
    preference_scope?: string,
    /** Whether the PII principal prefers anonymous processing where possible. */
    anonymity_preference?: boolean,
    /** Whether the PII principal prefers pseudonymous processing where possible. */
    pseudonymity_preference?: boolean,
    /** Specific processing operations the PII principal wishes to restrict. */
    processing_restriction_preferences?: string,
    /** Restrictions on disclosing PII to specific parties or categories of parties. */
    disclosure_restriction_preferences?: string[],
    /** Date when these privacy preferences were recorded. */
    preference_recorded_date?: date,
}



