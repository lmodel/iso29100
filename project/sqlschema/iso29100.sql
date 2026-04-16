-- # Abstract Class: NamedEntity Description: Abstract base class for all entities with a unique identifier, name, and description. Provides common identification and documentation slots.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity record was created.
--     * Slot: modified_date Description: Date when the entity record was last modified.
-- # Class: PrivacyFramework Description: Top-level container representing an organization's privacy framework for protecting PII within ICT systems.
--     * Slot: organization_name Description: Name of the organization operating the privacy framework.
--     * Slot: ict_system_description Description: Description of the ICT system(s) within the scope of the privacy framework.
--     * Slot: pii_principals_description Description: Description of the categories of PII principals whose PII is processed.
--     * Slot: privacy_policy Description: The organization's privacy policy governing PII processing.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity record was created.
--     * Slot: modified_date Description: Date when the entity record was last modified.
-- # Abstract Class: PrivacyStakeholder Description: Schema base class for the four actor types recognized by the privacy framework: PII principals, PII controllers, PII processors, and third parties. Provides shared contact and jurisdictional attributes common to all stakeholder roles.
--     * Slot: contact_information Description: Contact details for the privacy stakeholder.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity record was created.
--     * Slot: modified_date Description: Date when the entity record was last modified.
-- # Class: PIIPrincipal Description: Schema class for a data subject — the individual to whom PII belongs. Links consent records and privacy preferences to the natural person whose data is being processed, enabling subject-centric data models.
--     * Slot: contact_information Description: Contact details for the privacy stakeholder.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity record was created.
--     * Slot: modified_date Description: Date when the entity record was last modified.
-- # Class: PIIController Description: Schema class for an organization or individual that determines why and how PII is processed. Captures appointed processors, legal bases relied upon, privacy policy reference, and data protection officer details. Bears ultimate accountability for privacy principle adherence.
--     * Slot: privacy_policy_ref Description: Reference to the privacy policy of this PII controller.
--     * Slot: data_protection_officer Description: Name or contact of the data protection officer, where applicable.
--     * Slot: contact_information Description: Contact details for the privacy stakeholder.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity record was created.
--     * Slot: modified_date Description: Date when the entity record was last modified.
--     * Slot: PrivacyFramework_id Description: Autocreated FK slot
-- # Class: PIIProcessor Description: Schema class for an organization engaged to process PII under a PII controller's instructions. Records the instructing controller, data processing agreement reference, and any sub-processors engaged on the controller's behalf.
--     * Slot: instructing_controller Description: The PII controller on whose behalf this processor acts.
--     * Slot: processing_agreement_ref Description: Reference to the data processing agreement with the controller.
--     * Slot: contact_information Description: Contact details for the privacy stakeholder.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity record was created.
--     * Slot: modified_date Description: Date when the entity record was last modified.
--     * Slot: PrivacyFramework_id Description: Autocreated FK slot
-- # Class: ThirdParty Description: Schema class for an external entity that receives PII outside the PII processor relationship — i.e., as a recipient that typically becomes a PII controller in its own right. Captures the receiving purpose and the legal basis for the transfer.
--     * Slot: receiving_purpose Description: Purpose for which the third party receives PII.
--     * Slot: transfer_basis Description: Legal or contractual basis for transferring PII to this third party.
--     * Slot: contact_information Description: Contact details for the privacy stakeholder.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity record was created.
--     * Slot: modified_date Description: Date when the entity record was last modified.
--     * Slot: PrivacyFramework_id Description: Autocreated FK slot
-- # Class: PersonallyIdentifiableInformation Description: Schema class representing a data element or attribute set that can be linked back to a natural person — either directly or through combination with other attributes. Captures sensitivity classification, identifier type, pseudonymization status, retention schedule, and processing operations applicable to the data.
--     * Slot: sensitivity_level Description: Sensitivity classification of this PII.
--     * Slot: identifier_type Description: Type of identifier (e.g., direct identifier, indirect identifier, linkable attribute, or combination of attributes).
--     * Slot: is_pseudonymized Description: Whether the PII has been pseudonymized.
--     * Slot: is_anonymized Description: Whether the PII has been anonymized. Anonymized data is no longer considered PII as the PII principal can no longer be identified.
--     * Slot: linkability_risk Description: Assessment of the risk that this data can be linked to identify a PII principal, even if not directly identifying on its own.
--     * Slot: applicable_to_principal Description: Reference or description of the PII principal(s) to whom this PII relates.
--     * Slot: retention_schedule Description: Schedule defining how long this PII is retained and how it is disposed.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity record was created.
--     * Slot: modified_date Description: Date when the entity record was last modified.
-- # Class: PIIFlowScenario Description: A documented scenario describing the flow of PII among privacy framework actors (PII principal, PII controller, PII processor, and third party), as illustrated in Table 1 of Clause 5.3.
--     * Slot: scenario_label Description: Label for the PII flow scenario (e.g., "Scenario a").
--     * Slot: pii_principal_role Description: Role of the PII principal in this flow scenario.
--     * Slot: pii_controller_role Description: Role of the PII controller in this flow scenario.
--     * Slot: pii_processor_role Description: Role of the PII processor in this flow scenario.
--     * Slot: third_party_role Description: Role of the third party in this flow scenario.
--     * Slot: scenario_description Description: Description of the PII flow scenario and when it occurs.
--     * Slot: legal_control_retention Description: Description of how legal control of PII is retained or transferred, relevant to distinguishing between a PII processor and a third party.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity record was created.
--     * Slot: modified_date Description: Date when the entity record was last modified.
-- # Class: PrivacySafeguardingRequirement Description: Schema class for an applicable requirement that drives an organization's PII processing controls. Requirements are identified through the privacy risk management process and arise from legal/regulatory, contractual, business, or other influencing factors.
--     * Slot: requirement_factor Description: Category of factor driving this safeguarding requirement.
--     * Slot: requirement_text Description: Organization-authored statement of the safeguarding requirement.
--     * Slot: source_reference Description: Reference to the source (e.g., law name, regulation, contract, or standard).
--     * Slot: priority Description: Priority level for addressing this requirement or risk.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity record was created.
--     * Slot: modified_date Description: Date when the entity record was last modified.
--     * Slot: PrivacyFramework_id Description: Autocreated FK slot
-- # Class: PrivacyPolicy Description: Schema class for a governing document expressing an organization's intentions and commitments for PII processing. Covers both the internal policy document and any external privacy notice made available to PII principals (referred to as a notice in this framework).
--     * Slot: policy_version Description: Version identifier for the privacy policy.
--     * Slot: effective_date Description: Date from which the privacy policy takes effect.
--     * Slot: policy_scope Description: Scope of the privacy policy (systems, activities, or organizations covered).
--     * Slot: data_retention_statement Description: Statement on how long PII is retained and how it is disposed.
--     * Slot: contact_for_inquiries Description: Contact information for PII-related inquiries from PII principals.
--     * Slot: last_review_date Description: Date when the policy was last reviewed.
--     * Slot: is_external_notice Description: Whether this is an external privacy notice (available to PII principals) rather than an internal policy document.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity record was created.
--     * Slot: modified_date Description: Date when the entity record was last modified.
-- # Class: PrivacyControl Description: Schema class for a protective measure that manages privacy risks within the framework. Can be organizational, physical, technical (including Privacy Enhancing Technologies), or legal-contractual in nature; linked to the principles and safeguarding requirements it addresses.
--     * Slot: control_type Description: Category of this privacy control.
--     * Slot: control_objective Description: The privacy objective this control is intended to achieve.
--     * Slot: implementation_description Description: Organization-authored description of how the control is implemented.
--     * Slot: responsible_actor Description: Actor responsible for implementing and maintaining this control.
--     * Slot: implementation_status Description: Current implementation status of the control.
--     * Slot: is_pet Description: Whether this control qualifies as a Privacy Enhancing Technology (PET): an ICT-based privacy control that protects privacy by minimizing, eliminating, or preventing unnecessary PII processing without reducing the intended functionality of the system.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity record was created.
--     * Slot: modified_date Description: Date when the entity record was last modified.
--     * Slot: PrivacyFramework_id Description: Autocreated FK slot
-- # Class: PrivacyRisk Description: Schema class representing a potential adverse outcome for PII principals from a PII processing activity. Captures the risk source, likelihood and impact assessments, inherent and residual risk levels, and links to mitigating controls and accountable risk owner.
--     * Slot: risk_source Description: Source or origin of the privacy risk.
--     * Slot: affected_principals_description Description: Description of PII principals who could be adversely affected.
--     * Slot: risk_likelihood Description: Assessed likelihood of this privacy risk materializing.
--     * Slot: risk_impact_description Description: Description of potential adverse consequences for PII principals.
--     * Slot: inherent_risk_level Description: Privacy risk level before controls are applied.
--     * Slot: residual_risk_level Description: Privacy risk level after controls are applied.
--     * Slot: risk_owner Description: Person accountable for managing this privacy risk.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity record was created.
--     * Slot: modified_date Description: Date when the entity record was last modified.
--     * Slot: PrivacyFramework_id Description: Autocreated FK slot
-- # Class: PrivacyImpactAssessment Description: Schema class for a structured evaluation of the privacy implications of a processing activity or ICT system. Records assessment scope, identified and treated risks, accepted residual risks, stakeholder consultation records, and overall assessment outcome.
--     * Slot: assessment_scope Description: Scope of the privacy impact assessment.
--     * Slot: assessment_date Description: Date the assessment was conducted.
--     * Slot: assessor Description: Person or team who conducted the assessment.
--     * Slot: assessment_outcome Description: Overall outcome and conclusions of the privacy impact assessment.
--     * Slot: next_assessment_date Description: Planned date for the next assessment.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity record was created.
--     * Slot: modified_date Description: Date when the entity record was last modified.
--     * Slot: PrivacyFramework_id Description: Autocreated FK slot
-- # Class: PrivacyBreach Description: Schema class for a recorded incident in which PII was processed in a manner that violates applicable privacy safeguarding requirements. Tracks breach details, affected PII categories, notification obligations, remediation actions, and lessons learned.
--     * Slot: breach_datetime Description: Date and time when the privacy breach occurred.
--     * Slot: discovery_datetime Description: Date and time when the privacy breach was discovered.
--     * Slot: breach_description Description: Description of the privacy breach and the violated requirements.
--     * Slot: affected_principals_count Description: Estimated number of PII principals whose PII was involved.
--     * Slot: breach_severity Description: Assessed severity of the privacy breach.
--     * Slot: notification_required Description: Whether notification to authorities or PII principals was required.
--     * Slot: lessons_learned Description: Lessons learned from the breach to improve privacy controls.
--     * Slot: closure_datetime Description: Date and time when the breach record was closed.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity record was created.
--     * Slot: modified_date Description: Date when the entity record was last modified.
--     * Slot: PrivacyFramework_id Description: Autocreated FK slot
-- # Class: PIIProcessingActivity Description: Schema class documenting a PII processing operation: its purpose, legal basis, operation types performed, categories of PII involved, responsible actors, applied controls, retention period, and any cross-border transfer safeguards.
--     * Slot: processing_purpose Description: The specific, explicit, and legitimate purpose for this processing activity.
--     * Slot: legal_basis Description: Legal basis relied upon for this processing activity.
--     * Slot: controller_ref Description: PII controller responsible for this processing activity.
--     * Slot: processor_ref Description: PII processor performing this processing activity, if applicable.
--     * Slot: retention_period Description: Retention period for PII processed in this activity.
--     * Slot: cross_border_transfer Description: Whether this activity involves cross-border transfer of PII.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity record was created.
--     * Slot: modified_date Description: Date when the entity record was last modified.
--     * Slot: PrivacyFramework_id Description: Autocreated FK slot
-- # Class: PrivacyPrincipleImplementation Description: Documentation of how a specific privacy principle from Clause 6 has been implemented within the organization's privacy framework, including measures taken and evidence of adherence.
--     * Slot: principle Description: The privacy principle being implemented.
--     * Slot: last_assessed_date Description: Date when adherence to this principle was last assessed.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity record was created.
--     * Slot: modified_date Description: Date when the entity record was last modified.
--     * Slot: PrivacyFramework_id Description: Autocreated FK slot
-- # Class: ConsentRecord Description: Schema class documenting a PII principal's agreement to processing of their PII for stated purposes. Records the consent mechanism used, scope, current status, and withdrawal date — supporting auditability of the consent and choice privacy principle.
--     * Slot: principal_ref Description: Reference to the PII principal associated with this consent record or privacy preference.
--     * Slot: consent_date Description: Date and time when consent was given.
--     * Slot: consent_mechanism Description: Mechanism by which consent was obtained.
--     * Slot: withdrawal_date Description: Date and time when consent was withdrawn, if applicable.
--     * Slot: consent_status Description: Current status of the consent.
--     * Slot: consent_evidence_ref Description: Reference to evidence of consent (e.g., record identifier or URL).
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity record was created.
--     * Slot: modified_date Description: Date when the entity record was last modified.
--     * Slot: PIIPrincipal_id Description: Autocreated FK slot
-- # Class: PrivacyPreference Description: Schema class capturing a PII principal's processing choices for a particular purpose scope: preferences for anonymity or pseudonymity, restrictions on specific processing operations, and restrictions on disclosure to named or categorized parties.
--     * Slot: principal_ref Description: Reference to the PII principal associated with this consent record or privacy preference.
--     * Slot: preference_scope Description: The processing activities or purposes to which these preferences apply.
--     * Slot: anonymity_preference Description: Whether the PII principal prefers anonymous processing where possible.
--     * Slot: pseudonymity_preference Description: Whether the PII principal prefers pseudonymous processing where possible.
--     * Slot: preference_recorded_date Description: Date when these privacy preferences were recorded.
--     * Slot: id Description: Unique identifier for this entity instance.
--     * Slot: name Description: Human-readable name or title.
--     * Slot: description Description: Detailed description of the entity.
--     * Slot: created_date Description: Date when the entity record was created.
--     * Slot: modified_date Description: Date when the entity record was last modified.
--     * Slot: PIIPrincipal_id Description: Autocreated FK slot
-- # Class: PrivacyFramework_applicable_jurisdictions
--     * Slot: PrivacyFramework_id Description: Autocreated FK slot
--     * Slot: applicable_jurisdictions Description: Legal jurisdictions whose privacy laws apply to the organization.
-- # Class: PrivacyStakeholder_jurisdictions
--     * Slot: PrivacyStakeholder_id Description: Autocreated FK slot
--     * Slot: jurisdictions Description: Jurisdictions in which the privacy stakeholder operates.
-- # Class: PIIPrincipal_jurisdictions
--     * Slot: PIIPrincipal_id Description: Autocreated FK slot
--     * Slot: jurisdictions Description: Jurisdictions in which the privacy stakeholder operates.
-- # Class: PIIController_processing_purposes
--     * Slot: PIIController_id Description: Autocreated FK slot
--     * Slot: processing_purposes Description: Purposes for which the PII controller processes PII.
-- # Class: PIIController_legal_bases
--     * Slot: PIIController_id Description: Autocreated FK slot
--     * Slot: legal_bases Description: Legal bases relied upon for PII processing by this controller.
-- # Class: PIIController_appointed_processors
--     * Slot: PIIController_id Description: Autocreated FK slot
--     * Slot: appointed_processors_id Description: PII processors appointed by this controller.
-- # Class: PIIController_jurisdictions
--     * Slot: PIIController_id Description: Autocreated FK slot
--     * Slot: jurisdictions Description: Jurisdictions in which the privacy stakeholder operates.
-- # Class: PIIProcessor_sub_processors
--     * Slot: PIIProcessor_id Description: Autocreated FK slot
--     * Slot: sub_processors_id Description: Sub-processors engaged by this PII processor.
-- # Class: PIIProcessor_jurisdictions
--     * Slot: PIIProcessor_id Description: Autocreated FK slot
--     * Slot: jurisdictions Description: Jurisdictions in which the privacy stakeholder operates.
-- # Class: ThirdParty_jurisdictions
--     * Slot: ThirdParty_id Description: Autocreated FK slot
--     * Slot: jurisdictions Description: Jurisdictions in which the privacy stakeholder operates.
-- # Class: PersonallyIdentifiableInformation_pii_category
--     * Slot: PersonallyIdentifiableInformation_id Description: Autocreated FK slot
--     * Slot: pii_category Description: Category or type of PII (e.g., financial, health, biometric, location).
-- # Class: PersonallyIdentifiableInformation_processing_operations
--     * Slot: PersonallyIdentifiableInformation_id Description: Autocreated FK slot
--     * Slot: processing_operations Description: Types of processing operations performed on this PII.
-- # Class: PrivacySafeguardingRequirement_applicable_to_actors
--     * Slot: PrivacySafeguardingRequirement_id Description: Autocreated FK slot
--     * Slot: applicable_to_actors Description: Privacy stakeholder roles to which this requirement applies.
-- # Class: PrivacySafeguardingRequirement_related_controls
--     * Slot: PrivacySafeguardingRequirement_id Description: Autocreated FK slot
--     * Slot: related_controls_id Description: Privacy controls that implement or contribute to this requirement.
-- # Class: PrivacyPolicy_processing_purposes_covered
--     * Slot: PrivacyPolicy_id Description: Autocreated FK slot
--     * Slot: processing_purposes_covered Description: Processing purposes addressed by this privacy policy.
-- # Class: PrivacyPolicy_pii_categories_covered
--     * Slot: PrivacyPolicy_id Description: Autocreated FK slot
--     * Slot: pii_categories_covered Description: Categories of PII addressed by this privacy policy.
-- # Class: PrivacyPolicy_pii_principal_rights
--     * Slot: PrivacyPolicy_id Description: Autocreated FK slot
--     * Slot: pii_principal_rights Description: Rights available to PII principals under this policy.
-- # Class: PrivacyPolicy_applicable_principles
--     * Slot: PrivacyPolicy_id Description: Autocreated FK slot
--     * Slot: applicable_principles Description: Privacy principles this policy addresses.
-- # Class: PrivacyControl_addressed_principles
--     * Slot: PrivacyControl_id Description: Autocreated FK slot
--     * Slot: addressed_principles Description: Privacy principles this control helps implement.
-- # Class: PrivacyControl_effectiveness_evidence
--     * Slot: PrivacyControl_id Description: Autocreated FK slot
--     * Slot: effectiveness_evidence Description: Evidence of control effectiveness.
-- # Class: PrivacyControl_related_safeguarding_requirements
--     * Slot: PrivacyControl_id Description: Autocreated FK slot
--     * Slot: related_safeguarding_requirements_id Description: Safeguarding requirements this control addresses.
-- # Class: PrivacyRisk_affected_pii_categories
--     * Slot: PrivacyRisk_id Description: Autocreated FK slot
--     * Slot: affected_pii_categories Description: Categories of PII affected by this privacy risk or breach.
-- # Class: PrivacyRisk_mitigating_controls
--     * Slot: PrivacyRisk_id Description: Autocreated FK slot
--     * Slot: mitigating_controls_id Description: Privacy controls that mitigate this risk.
-- # Class: PrivacyImpactAssessment_processing_activities_assessed
--     * Slot: PrivacyImpactAssessment_id Description: Autocreated FK slot
--     * Slot: processing_activities_assessed_id Description: PII processing activities reviewed in this assessment.
-- # Class: PrivacyImpactAssessment_risks_identified
--     * Slot: PrivacyImpactAssessment_id Description: Autocreated FK slot
--     * Slot: risks_identified_id Description: Privacy risks identified during this assessment.
-- # Class: PrivacyImpactAssessment_risks_treated
--     * Slot: PrivacyImpactAssessment_id Description: Autocreated FK slot
--     * Slot: risks_treated_id Description: Privacy risks for which treatment was planned or applied.
-- # Class: PrivacyImpactAssessment_residual_risks_accepted
--     * Slot: PrivacyImpactAssessment_id Description: Autocreated FK slot
--     * Slot: residual_risks_accepted_id Description: Privacy risks accepted as residual after treatment.
-- # Class: PrivacyImpactAssessment_consultation_records
--     * Slot: PrivacyImpactAssessment_id Description: Autocreated FK slot
--     * Slot: consultation_records Description: Records of stakeholder consultations conducted during the assessment.
-- # Class: PrivacyBreach_affected_pii_categories
--     * Slot: PrivacyBreach_id Description: Autocreated FK slot
--     * Slot: affected_pii_categories Description: Categories of PII affected by this privacy risk or breach.
-- # Class: PrivacyBreach_violated_requirements
--     * Slot: PrivacyBreach_id Description: Autocreated FK slot
--     * Slot: violated_requirements_id Description: Privacy safeguarding requirements violated by this breach.
-- # Class: PrivacyBreach_immediate_actions
--     * Slot: PrivacyBreach_id Description: Autocreated FK slot
--     * Slot: immediate_actions Description: Immediate actions taken to contain the breach.
-- # Class: PrivacyBreach_notifications_made
--     * Slot: PrivacyBreach_id Description: Autocreated FK slot
--     * Slot: notifications_made Description: Notifications made to authorities, PII principals, or other parties.
-- # Class: PrivacyBreach_remediation_actions
--     * Slot: PrivacyBreach_id Description: Autocreated FK slot
--     * Slot: remediation_actions Description: Actions taken to remediate the breach and prevent recurrence.
-- # Class: PIIProcessingActivity_operations_performed
--     * Slot: PIIProcessingActivity_id Description: Autocreated FK slot
--     * Slot: operations_performed Description: Processing operations performed in this activity.
-- # Class: PIIProcessingActivity_pii_categories_processed
--     * Slot: PIIProcessingActivity_id Description: Autocreated FK slot
--     * Slot: pii_categories_processed Description: Categories of PII processed in this activity.
-- # Class: PIIProcessingActivity_sensitivity_levels_involved
--     * Slot: PIIProcessingActivity_id Description: Autocreated FK slot
--     * Slot: sensitivity_levels_involved Description: Sensitivity levels of PII processed in this activity.
-- # Class: PIIProcessingActivity_data_flows
--     * Slot: PIIProcessingActivity_id Description: Autocreated FK slot
--     * Slot: data_flows_id Description: PII flow scenarios applicable to this processing activity.
-- # Class: PIIProcessingActivity_privacy_controls_applied
--     * Slot: PIIProcessingActivity_id Description: Autocreated FK slot
--     * Slot: privacy_controls_applied_id Description: Privacy controls applied to this processing activity.
-- # Class: PIIProcessingActivity_transfer_safeguards
--     * Slot: PIIProcessingActivity_id Description: Autocreated FK slot
--     * Slot: transfer_safeguards Description: Safeguards in place for cross-border PII transfers.
-- # Class: PrivacyPrincipleImplementation_implementation_measures
--     * Slot: PrivacyPrincipleImplementation_id Description: Autocreated FK slot
--     * Slot: implementation_measures Description: Measures taken to implement this privacy principle.
-- # Class: PrivacyPrincipleImplementation_applicable_controls_ref
--     * Slot: PrivacyPrincipleImplementation_id Description: Autocreated FK slot
--     * Slot: applicable_controls_ref_id Description: Privacy controls that contribute to implementing this principle.
-- # Class: PrivacyPrincipleImplementation_evidence_of_adherence
--     * Slot: PrivacyPrincipleImplementation_id Description: Autocreated FK slot
--     * Slot: evidence_of_adherence Description: Evidence demonstrating adherence to this principle.
-- # Class: PrivacyPrincipleImplementation_gaps_identified
--     * Slot: PrivacyPrincipleImplementation_id Description: Autocreated FK slot
--     * Slot: gaps_identified Description: Identified gaps in the implementation of this principle.
-- # Class: PrivacyPrincipleImplementation_improvement_actions
--     * Slot: PrivacyPrincipleImplementation_id Description: Autocreated FK slot
--     * Slot: improvement_actions Description: Actions planned to address identified implementation gaps.
-- # Class: ConsentRecord_processing_purposes_consented
--     * Slot: ConsentRecord_id Description: Autocreated FK slot
--     * Slot: processing_purposes_consented Description: Processing purposes for which consent was given.
-- # Class: ConsentRecord_pii_categories_consented
--     * Slot: ConsentRecord_id Description: Autocreated FK slot
--     * Slot: pii_categories_consented Description: Categories of PII for which consent was given.
-- # Class: PrivacyPreference_processing_restriction_preferences
--     * Slot: PrivacyPreference_id Description: Autocreated FK slot
--     * Slot: processing_restriction_preferences Description: Specific processing operations the PII principal wishes to restrict.
-- # Class: PrivacyPreference_disclosure_restriction_preferences
--     * Slot: PrivacyPreference_id Description: Autocreated FK slot
--     * Slot: disclosure_restriction_preferences Description: Restrictions on disclosing PII to specific parties or categories of parties.

CREATE TABLE "NamedEntity" (
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_NamedEntity_id" ON "NamedEntity" (id);

CREATE TABLE "PrivacyStakeholder" (
	contact_information TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_PrivacyStakeholder_id" ON "PrivacyStakeholder" (id);

CREATE TABLE "PIIPrincipal" (
	contact_information TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_PIIPrincipal_id" ON "PIIPrincipal" (id);

CREATE TABLE "PersonallyIdentifiableInformation" (
	sensitivity_level VARCHAR(9),
	identifier_type TEXT,
	is_pseudonymized BOOLEAN,
	is_anonymized BOOLEAN,
	linkability_risk TEXT,
	applicable_to_principal TEXT,
	retention_schedule TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_PersonallyIdentifiableInformation_id" ON "PersonallyIdentifiableInformation" (id);

CREATE TABLE "PIIFlowScenario" (
	scenario_label TEXT,
	pii_principal_role VARCHAR(13),
	pii_controller_role VARCHAR(13),
	pii_processor_role VARCHAR(13),
	third_party_role VARCHAR(13),
	scenario_description TEXT,
	legal_control_retention TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_PIIFlowScenario_id" ON "PIIFlowScenario" (id);

CREATE TABLE "PrivacyPolicy" (
	policy_version TEXT,
	effective_date DATE,
	policy_scope TEXT,
	data_retention_statement TEXT,
	contact_for_inquiries TEXT,
	last_review_date DATE,
	is_external_notice BOOLEAN,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_PrivacyPolicy_id" ON "PrivacyPolicy" (id);

CREATE TABLE "PrivacyFramework" (
	organization_name TEXT,
	ict_system_description TEXT,
	pii_principals_description TEXT,
	privacy_policy TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	PRIMARY KEY (id),
	FOREIGN KEY(privacy_policy) REFERENCES "PrivacyPolicy" (id)
);
CREATE INDEX "ix_PrivacyFramework_id" ON "PrivacyFramework" (id);

CREATE TABLE "ConsentRecord" (
	principal_ref TEXT,
	consent_date DATETIME,
	consent_mechanism VARCHAR(7),
	withdrawal_date DATETIME,
	consent_status TEXT,
	consent_evidence_ref TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	"PIIPrincipal_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("PIIPrincipal_id") REFERENCES "PIIPrincipal" (id)
);
CREATE INDEX "ix_ConsentRecord_id" ON "ConsentRecord" (id);

CREATE TABLE "PrivacyPreference" (
	principal_ref TEXT,
	preference_scope TEXT,
	anonymity_preference BOOLEAN,
	pseudonymity_preference BOOLEAN,
	preference_recorded_date DATE,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	"PIIPrincipal_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("PIIPrincipal_id") REFERENCES "PIIPrincipal" (id)
);
CREATE INDEX "ix_PrivacyPreference_id" ON "PrivacyPreference" (id);

CREATE TABLE "PrivacyStakeholder_jurisdictions" (
	"PrivacyStakeholder_id" TEXT,
	jurisdictions TEXT,
	PRIMARY KEY ("PrivacyStakeholder_id", jurisdictions),
	FOREIGN KEY("PrivacyStakeholder_id") REFERENCES "PrivacyStakeholder" (id)
);
CREATE INDEX "ix_PrivacyStakeholder_jurisdictions_PrivacyStakeholder_id" ON "PrivacyStakeholder_jurisdictions" ("PrivacyStakeholder_id");
CREATE INDEX "ix_PrivacyStakeholder_jurisdictions_jurisdictions" ON "PrivacyStakeholder_jurisdictions" (jurisdictions);

CREATE TABLE "PIIPrincipal_jurisdictions" (
	"PIIPrincipal_id" TEXT,
	jurisdictions TEXT,
	PRIMARY KEY ("PIIPrincipal_id", jurisdictions),
	FOREIGN KEY("PIIPrincipal_id") REFERENCES "PIIPrincipal" (id)
);
CREATE INDEX "ix_PIIPrincipal_jurisdictions_PIIPrincipal_id" ON "PIIPrincipal_jurisdictions" ("PIIPrincipal_id");
CREATE INDEX "ix_PIIPrincipal_jurisdictions_jurisdictions" ON "PIIPrincipal_jurisdictions" (jurisdictions);

CREATE TABLE "PersonallyIdentifiableInformation_pii_category" (
	"PersonallyIdentifiableInformation_id" TEXT,
	pii_category TEXT,
	PRIMARY KEY ("PersonallyIdentifiableInformation_id", pii_category),
	FOREIGN KEY("PersonallyIdentifiableInformation_id") REFERENCES "PersonallyIdentifiableInformation" (id)
);
CREATE INDEX "ix_PersonallyIdentifiableInformation_pii_category_PersonallyIdentifiableInformation_id" ON "PersonallyIdentifiableInformation_pii_category" ("PersonallyIdentifiableInformation_id");
CREATE INDEX "ix_PersonallyIdentifiableInformation_pii_category_pii_category" ON "PersonallyIdentifiableInformation_pii_category" (pii_category);

CREATE TABLE "PersonallyIdentifiableInformation_processing_operations" (
	"PersonallyIdentifiableInformation_id" TEXT,
	processing_operations VARCHAR(16),
	PRIMARY KEY ("PersonallyIdentifiableInformation_id", processing_operations),
	FOREIGN KEY("PersonallyIdentifiableInformation_id") REFERENCES "PersonallyIdentifiableInformation" (id)
);
CREATE INDEX "ix_PersonallyIdentifiableInformation_processing_operations_PersonallyIdentifiableInformation_id" ON "PersonallyIdentifiableInformation_processing_operations" ("PersonallyIdentifiableInformation_id");
CREATE INDEX "ix_PersonallyIdentifiableInformation_processing_operations_processing_operations" ON "PersonallyIdentifiableInformation_processing_operations" (processing_operations);

CREATE TABLE "PrivacyPolicy_processing_purposes_covered" (
	"PrivacyPolicy_id" TEXT,
	processing_purposes_covered TEXT,
	PRIMARY KEY ("PrivacyPolicy_id", processing_purposes_covered),
	FOREIGN KEY("PrivacyPolicy_id") REFERENCES "PrivacyPolicy" (id)
);
CREATE INDEX "ix_PrivacyPolicy_processing_purposes_covered_processing_purposes_covered" ON "PrivacyPolicy_processing_purposes_covered" (processing_purposes_covered);
CREATE INDEX "ix_PrivacyPolicy_processing_purposes_covered_PrivacyPolicy_id" ON "PrivacyPolicy_processing_purposes_covered" ("PrivacyPolicy_id");

CREATE TABLE "PrivacyPolicy_pii_categories_covered" (
	"PrivacyPolicy_id" TEXT,
	pii_categories_covered TEXT,
	PRIMARY KEY ("PrivacyPolicy_id", pii_categories_covered),
	FOREIGN KEY("PrivacyPolicy_id") REFERENCES "PrivacyPolicy" (id)
);
CREATE INDEX "ix_PrivacyPolicy_pii_categories_covered_PrivacyPolicy_id" ON "PrivacyPolicy_pii_categories_covered" ("PrivacyPolicy_id");
CREATE INDEX "ix_PrivacyPolicy_pii_categories_covered_pii_categories_covered" ON "PrivacyPolicy_pii_categories_covered" (pii_categories_covered);

CREATE TABLE "PrivacyPolicy_pii_principal_rights" (
	"PrivacyPolicy_id" TEXT,
	pii_principal_rights TEXT,
	PRIMARY KEY ("PrivacyPolicy_id", pii_principal_rights),
	FOREIGN KEY("PrivacyPolicy_id") REFERENCES "PrivacyPolicy" (id)
);
CREATE INDEX "ix_PrivacyPolicy_pii_principal_rights_PrivacyPolicy_id" ON "PrivacyPolicy_pii_principal_rights" ("PrivacyPolicy_id");
CREATE INDEX "ix_PrivacyPolicy_pii_principal_rights_pii_principal_rights" ON "PrivacyPolicy_pii_principal_rights" (pii_principal_rights);

CREATE TABLE "PrivacyPolicy_applicable_principles" (
	"PrivacyPolicy_id" TEXT,
	applicable_principles VARCHAR(39),
	PRIMARY KEY ("PrivacyPolicy_id", applicable_principles),
	FOREIGN KEY("PrivacyPolicy_id") REFERENCES "PrivacyPolicy" (id)
);
CREATE INDEX "ix_PrivacyPolicy_applicable_principles_applicable_principles" ON "PrivacyPolicy_applicable_principles" (applicable_principles);
CREATE INDEX "ix_PrivacyPolicy_applicable_principles_PrivacyPolicy_id" ON "PrivacyPolicy_applicable_principles" ("PrivacyPolicy_id");

CREATE TABLE "PIIController" (
	privacy_policy_ref TEXT,
	data_protection_officer TEXT,
	contact_information TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	"PrivacyFramework_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(privacy_policy_ref) REFERENCES "PrivacyPolicy" (id),
	FOREIGN KEY("PrivacyFramework_id") REFERENCES "PrivacyFramework" (id)
);
CREATE INDEX "ix_PIIController_id" ON "PIIController" (id);

CREATE TABLE "ThirdParty" (
	receiving_purpose TEXT,
	transfer_basis TEXT,
	contact_information TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	"PrivacyFramework_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("PrivacyFramework_id") REFERENCES "PrivacyFramework" (id)
);
CREATE INDEX "ix_ThirdParty_id" ON "ThirdParty" (id);

CREATE TABLE "PrivacySafeguardingRequirement" (
	requirement_factor VARCHAR(20),
	requirement_text TEXT,
	source_reference TEXT,
	priority TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	"PrivacyFramework_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("PrivacyFramework_id") REFERENCES "PrivacyFramework" (id)
);
CREATE INDEX "ix_PrivacySafeguardingRequirement_id" ON "PrivacySafeguardingRequirement" (id);

CREATE TABLE "PrivacyControl" (
	control_type VARCHAR(17),
	control_objective TEXT,
	implementation_description TEXT,
	responsible_actor TEXT,
	implementation_status TEXT,
	is_pet BOOLEAN,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	"PrivacyFramework_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("PrivacyFramework_id") REFERENCES "PrivacyFramework" (id)
);
CREATE INDEX "ix_PrivacyControl_id" ON "PrivacyControl" (id);

CREATE TABLE "PrivacyRisk" (
	risk_source TEXT,
	affected_principals_description TEXT,
	risk_likelihood TEXT,
	risk_impact_description TEXT,
	inherent_risk_level VARCHAR(9),
	residual_risk_level VARCHAR(9),
	risk_owner TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	"PrivacyFramework_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("PrivacyFramework_id") REFERENCES "PrivacyFramework" (id)
);
CREATE INDEX "ix_PrivacyRisk_id" ON "PrivacyRisk" (id);

CREATE TABLE "PrivacyImpactAssessment" (
	assessment_scope TEXT,
	assessment_date DATE,
	assessor TEXT,
	assessment_outcome TEXT,
	next_assessment_date DATE,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	"PrivacyFramework_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("PrivacyFramework_id") REFERENCES "PrivacyFramework" (id)
);
CREATE INDEX "ix_PrivacyImpactAssessment_id" ON "PrivacyImpactAssessment" (id);

CREATE TABLE "PrivacyBreach" (
	breach_datetime DATETIME,
	discovery_datetime DATETIME,
	breach_description TEXT,
	affected_principals_count INTEGER,
	breach_severity VARCHAR(9),
	notification_required BOOLEAN,
	lessons_learned TEXT,
	closure_datetime DATETIME,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	"PrivacyFramework_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("PrivacyFramework_id") REFERENCES "PrivacyFramework" (id)
);
CREATE INDEX "ix_PrivacyBreach_id" ON "PrivacyBreach" (id);

CREATE TABLE "PrivacyPrincipleImplementation" (
	principle VARCHAR(39) NOT NULL,
	last_assessed_date DATE,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	"PrivacyFramework_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("PrivacyFramework_id") REFERENCES "PrivacyFramework" (id)
);
CREATE INDEX "ix_PrivacyPrincipleImplementation_id" ON "PrivacyPrincipleImplementation" (id);

CREATE TABLE "PrivacyFramework_applicable_jurisdictions" (
	"PrivacyFramework_id" TEXT,
	applicable_jurisdictions TEXT,
	PRIMARY KEY ("PrivacyFramework_id", applicable_jurisdictions),
	FOREIGN KEY("PrivacyFramework_id") REFERENCES "PrivacyFramework" (id)
);
CREATE INDEX "ix_PrivacyFramework_applicable_jurisdictions_PrivacyFramework_id" ON "PrivacyFramework_applicable_jurisdictions" ("PrivacyFramework_id");
CREATE INDEX "ix_PrivacyFramework_applicable_jurisdictions_applicable_jurisdictions" ON "PrivacyFramework_applicable_jurisdictions" (applicable_jurisdictions);

CREATE TABLE "ConsentRecord_processing_purposes_consented" (
	"ConsentRecord_id" TEXT,
	processing_purposes_consented TEXT,
	PRIMARY KEY ("ConsentRecord_id", processing_purposes_consented),
	FOREIGN KEY("ConsentRecord_id") REFERENCES "ConsentRecord" (id)
);
CREATE INDEX "ix_ConsentRecord_processing_purposes_consented_processing_purposes_consented" ON "ConsentRecord_processing_purposes_consented" (processing_purposes_consented);
CREATE INDEX "ix_ConsentRecord_processing_purposes_consented_ConsentRecord_id" ON "ConsentRecord_processing_purposes_consented" ("ConsentRecord_id");

CREATE TABLE "ConsentRecord_pii_categories_consented" (
	"ConsentRecord_id" TEXT,
	pii_categories_consented TEXT,
	PRIMARY KEY ("ConsentRecord_id", pii_categories_consented),
	FOREIGN KEY("ConsentRecord_id") REFERENCES "ConsentRecord" (id)
);
CREATE INDEX "ix_ConsentRecord_pii_categories_consented_pii_categories_consented" ON "ConsentRecord_pii_categories_consented" (pii_categories_consented);
CREATE INDEX "ix_ConsentRecord_pii_categories_consented_ConsentRecord_id" ON "ConsentRecord_pii_categories_consented" ("ConsentRecord_id");

CREATE TABLE "PrivacyPreference_processing_restriction_preferences" (
	"PrivacyPreference_id" TEXT,
	processing_restriction_preferences VARCHAR(16),
	PRIMARY KEY ("PrivacyPreference_id", processing_restriction_preferences),
	FOREIGN KEY("PrivacyPreference_id") REFERENCES "PrivacyPreference" (id)
);
CREATE INDEX "ix_PrivacyPreference_processing_restriction_preferences_PrivacyPreference_id" ON "PrivacyPreference_processing_restriction_preferences" ("PrivacyPreference_id");
CREATE INDEX "ix_PrivacyPreference_processing_restriction_preferences_processing_restriction_preferences" ON "PrivacyPreference_processing_restriction_preferences" (processing_restriction_preferences);

CREATE TABLE "PrivacyPreference_disclosure_restriction_preferences" (
	"PrivacyPreference_id" TEXT,
	disclosure_restriction_preferences TEXT,
	PRIMARY KEY ("PrivacyPreference_id", disclosure_restriction_preferences),
	FOREIGN KEY("PrivacyPreference_id") REFERENCES "PrivacyPreference" (id)
);
CREATE INDEX "ix_PrivacyPreference_disclosure_restriction_preferences_disclosure_restriction_preferences" ON "PrivacyPreference_disclosure_restriction_preferences" (disclosure_restriction_preferences);
CREATE INDEX "ix_PrivacyPreference_disclosure_restriction_preferences_PrivacyPreference_id" ON "PrivacyPreference_disclosure_restriction_preferences" ("PrivacyPreference_id");

CREATE TABLE "PIIProcessor" (
	instructing_controller TEXT,
	processing_agreement_ref TEXT,
	contact_information TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	"PrivacyFramework_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(instructing_controller) REFERENCES "PIIController" (id),
	FOREIGN KEY("PrivacyFramework_id") REFERENCES "PrivacyFramework" (id)
);
CREATE INDEX "ix_PIIProcessor_id" ON "PIIProcessor" (id);

CREATE TABLE "PIIController_processing_purposes" (
	"PIIController_id" TEXT,
	processing_purposes TEXT,
	PRIMARY KEY ("PIIController_id", processing_purposes),
	FOREIGN KEY("PIIController_id") REFERENCES "PIIController" (id)
);
CREATE INDEX "ix_PIIController_processing_purposes_PIIController_id" ON "PIIController_processing_purposes" ("PIIController_id");
CREATE INDEX "ix_PIIController_processing_purposes_processing_purposes" ON "PIIController_processing_purposes" (processing_purposes);

CREATE TABLE "PIIController_legal_bases" (
	"PIIController_id" TEXT,
	legal_bases TEXT,
	PRIMARY KEY ("PIIController_id", legal_bases),
	FOREIGN KEY("PIIController_id") REFERENCES "PIIController" (id)
);
CREATE INDEX "ix_PIIController_legal_bases_PIIController_id" ON "PIIController_legal_bases" ("PIIController_id");
CREATE INDEX "ix_PIIController_legal_bases_legal_bases" ON "PIIController_legal_bases" (legal_bases);

CREATE TABLE "PIIController_jurisdictions" (
	"PIIController_id" TEXT,
	jurisdictions TEXT,
	PRIMARY KEY ("PIIController_id", jurisdictions),
	FOREIGN KEY("PIIController_id") REFERENCES "PIIController" (id)
);
CREATE INDEX "ix_PIIController_jurisdictions_jurisdictions" ON "PIIController_jurisdictions" (jurisdictions);
CREATE INDEX "ix_PIIController_jurisdictions_PIIController_id" ON "PIIController_jurisdictions" ("PIIController_id");

CREATE TABLE "ThirdParty_jurisdictions" (
	"ThirdParty_id" TEXT,
	jurisdictions TEXT,
	PRIMARY KEY ("ThirdParty_id", jurisdictions),
	FOREIGN KEY("ThirdParty_id") REFERENCES "ThirdParty" (id)
);
CREATE INDEX "ix_ThirdParty_jurisdictions_ThirdParty_id" ON "ThirdParty_jurisdictions" ("ThirdParty_id");
CREATE INDEX "ix_ThirdParty_jurisdictions_jurisdictions" ON "ThirdParty_jurisdictions" (jurisdictions);

CREATE TABLE "PrivacySafeguardingRequirement_applicable_to_actors" (
	"PrivacySafeguardingRequirement_id" TEXT,
	applicable_to_actors TEXT,
	PRIMARY KEY ("PrivacySafeguardingRequirement_id", applicable_to_actors),
	FOREIGN KEY("PrivacySafeguardingRequirement_id") REFERENCES "PrivacySafeguardingRequirement" (id)
);
CREATE INDEX "ix_PrivacySafeguardingRequirement_applicable_to_actors_PrivacySafeguardingRequirement_id" ON "PrivacySafeguardingRequirement_applicable_to_actors" ("PrivacySafeguardingRequirement_id");
CREATE INDEX "ix_PrivacySafeguardingRequirement_applicable_to_actors_applicable_to_actors" ON "PrivacySafeguardingRequirement_applicable_to_actors" (applicable_to_actors);

CREATE TABLE "PrivacySafeguardingRequirement_related_controls" (
	"PrivacySafeguardingRequirement_id" TEXT,
	related_controls_id TEXT,
	PRIMARY KEY ("PrivacySafeguardingRequirement_id", related_controls_id),
	FOREIGN KEY("PrivacySafeguardingRequirement_id") REFERENCES "PrivacySafeguardingRequirement" (id),
	FOREIGN KEY(related_controls_id) REFERENCES "PrivacyControl" (id)
);
CREATE INDEX "ix_PrivacySafeguardingRequirement_related_controls_PrivacySafeguardingRequirement_id" ON "PrivacySafeguardingRequirement_related_controls" ("PrivacySafeguardingRequirement_id");
CREATE INDEX "ix_PrivacySafeguardingRequirement_related_controls_related_controls_id" ON "PrivacySafeguardingRequirement_related_controls" (related_controls_id);

CREATE TABLE "PrivacyControl_addressed_principles" (
	"PrivacyControl_id" TEXT,
	addressed_principles VARCHAR(39),
	PRIMARY KEY ("PrivacyControl_id", addressed_principles),
	FOREIGN KEY("PrivacyControl_id") REFERENCES "PrivacyControl" (id)
);
CREATE INDEX "ix_PrivacyControl_addressed_principles_addressed_principles" ON "PrivacyControl_addressed_principles" (addressed_principles);
CREATE INDEX "ix_PrivacyControl_addressed_principles_PrivacyControl_id" ON "PrivacyControl_addressed_principles" ("PrivacyControl_id");

CREATE TABLE "PrivacyControl_effectiveness_evidence" (
	"PrivacyControl_id" TEXT,
	effectiveness_evidence TEXT,
	PRIMARY KEY ("PrivacyControl_id", effectiveness_evidence),
	FOREIGN KEY("PrivacyControl_id") REFERENCES "PrivacyControl" (id)
);
CREATE INDEX "ix_PrivacyControl_effectiveness_evidence_effectiveness_evidence" ON "PrivacyControl_effectiveness_evidence" (effectiveness_evidence);
CREATE INDEX "ix_PrivacyControl_effectiveness_evidence_PrivacyControl_id" ON "PrivacyControl_effectiveness_evidence" ("PrivacyControl_id");

CREATE TABLE "PrivacyControl_related_safeguarding_requirements" (
	"PrivacyControl_id" TEXT,
	related_safeguarding_requirements_id TEXT,
	PRIMARY KEY ("PrivacyControl_id", related_safeguarding_requirements_id),
	FOREIGN KEY("PrivacyControl_id") REFERENCES "PrivacyControl" (id),
	FOREIGN KEY(related_safeguarding_requirements_id) REFERENCES "PrivacySafeguardingRequirement" (id)
);
CREATE INDEX "ix_PrivacyControl_related_safeguarding_requirements_related_safeguarding_requirements_id" ON "PrivacyControl_related_safeguarding_requirements" (related_safeguarding_requirements_id);
CREATE INDEX "ix_PrivacyControl_related_safeguarding_requirements_PrivacyControl_id" ON "PrivacyControl_related_safeguarding_requirements" ("PrivacyControl_id");

CREATE TABLE "PrivacyRisk_affected_pii_categories" (
	"PrivacyRisk_id" TEXT,
	affected_pii_categories TEXT,
	PRIMARY KEY ("PrivacyRisk_id", affected_pii_categories),
	FOREIGN KEY("PrivacyRisk_id") REFERENCES "PrivacyRisk" (id)
);
CREATE INDEX "ix_PrivacyRisk_affected_pii_categories_affected_pii_categories" ON "PrivacyRisk_affected_pii_categories" (affected_pii_categories);
CREATE INDEX "ix_PrivacyRisk_affected_pii_categories_PrivacyRisk_id" ON "PrivacyRisk_affected_pii_categories" ("PrivacyRisk_id");

CREATE TABLE "PrivacyRisk_mitigating_controls" (
	"PrivacyRisk_id" TEXT,
	mitigating_controls_id TEXT,
	PRIMARY KEY ("PrivacyRisk_id", mitigating_controls_id),
	FOREIGN KEY("PrivacyRisk_id") REFERENCES "PrivacyRisk" (id),
	FOREIGN KEY(mitigating_controls_id) REFERENCES "PrivacyControl" (id)
);
CREATE INDEX "ix_PrivacyRisk_mitigating_controls_mitigating_controls_id" ON "PrivacyRisk_mitigating_controls" (mitigating_controls_id);
CREATE INDEX "ix_PrivacyRisk_mitigating_controls_PrivacyRisk_id" ON "PrivacyRisk_mitigating_controls" ("PrivacyRisk_id");

CREATE TABLE "PrivacyImpactAssessment_risks_identified" (
	"PrivacyImpactAssessment_id" TEXT,
	risks_identified_id TEXT,
	PRIMARY KEY ("PrivacyImpactAssessment_id", risks_identified_id),
	FOREIGN KEY("PrivacyImpactAssessment_id") REFERENCES "PrivacyImpactAssessment" (id),
	FOREIGN KEY(risks_identified_id) REFERENCES "PrivacyRisk" (id)
);
CREATE INDEX "ix_PrivacyImpactAssessment_risks_identified_risks_identified_id" ON "PrivacyImpactAssessment_risks_identified" (risks_identified_id);
CREATE INDEX "ix_PrivacyImpactAssessment_risks_identified_PrivacyImpactAssessment_id" ON "PrivacyImpactAssessment_risks_identified" ("PrivacyImpactAssessment_id");

CREATE TABLE "PrivacyImpactAssessment_risks_treated" (
	"PrivacyImpactAssessment_id" TEXT,
	risks_treated_id TEXT,
	PRIMARY KEY ("PrivacyImpactAssessment_id", risks_treated_id),
	FOREIGN KEY("PrivacyImpactAssessment_id") REFERENCES "PrivacyImpactAssessment" (id),
	FOREIGN KEY(risks_treated_id) REFERENCES "PrivacyRisk" (id)
);
CREATE INDEX "ix_PrivacyImpactAssessment_risks_treated_PrivacyImpactAssessment_id" ON "PrivacyImpactAssessment_risks_treated" ("PrivacyImpactAssessment_id");
CREATE INDEX "ix_PrivacyImpactAssessment_risks_treated_risks_treated_id" ON "PrivacyImpactAssessment_risks_treated" (risks_treated_id);

CREATE TABLE "PrivacyImpactAssessment_residual_risks_accepted" (
	"PrivacyImpactAssessment_id" TEXT,
	residual_risks_accepted_id TEXT,
	PRIMARY KEY ("PrivacyImpactAssessment_id", residual_risks_accepted_id),
	FOREIGN KEY("PrivacyImpactAssessment_id") REFERENCES "PrivacyImpactAssessment" (id),
	FOREIGN KEY(residual_risks_accepted_id) REFERENCES "PrivacyRisk" (id)
);
CREATE INDEX "ix_PrivacyImpactAssessment_residual_risks_accepted_residual_risks_accepted_id" ON "PrivacyImpactAssessment_residual_risks_accepted" (residual_risks_accepted_id);
CREATE INDEX "ix_PrivacyImpactAssessment_residual_risks_accepted_PrivacyImpactAssessment_id" ON "PrivacyImpactAssessment_residual_risks_accepted" ("PrivacyImpactAssessment_id");

CREATE TABLE "PrivacyImpactAssessment_consultation_records" (
	"PrivacyImpactAssessment_id" TEXT,
	consultation_records TEXT,
	PRIMARY KEY ("PrivacyImpactAssessment_id", consultation_records),
	FOREIGN KEY("PrivacyImpactAssessment_id") REFERENCES "PrivacyImpactAssessment" (id)
);
CREATE INDEX "ix_PrivacyImpactAssessment_consultation_records_consultation_records" ON "PrivacyImpactAssessment_consultation_records" (consultation_records);
CREATE INDEX "ix_PrivacyImpactAssessment_consultation_records_PrivacyImpactAssessment_id" ON "PrivacyImpactAssessment_consultation_records" ("PrivacyImpactAssessment_id");

CREATE TABLE "PrivacyBreach_affected_pii_categories" (
	"PrivacyBreach_id" TEXT,
	affected_pii_categories TEXT,
	PRIMARY KEY ("PrivacyBreach_id", affected_pii_categories),
	FOREIGN KEY("PrivacyBreach_id") REFERENCES "PrivacyBreach" (id)
);
CREATE INDEX "ix_PrivacyBreach_affected_pii_categories_PrivacyBreach_id" ON "PrivacyBreach_affected_pii_categories" ("PrivacyBreach_id");
CREATE INDEX "ix_PrivacyBreach_affected_pii_categories_affected_pii_categories" ON "PrivacyBreach_affected_pii_categories" (affected_pii_categories);

CREATE TABLE "PrivacyBreach_violated_requirements" (
	"PrivacyBreach_id" TEXT,
	violated_requirements_id TEXT,
	PRIMARY KEY ("PrivacyBreach_id", violated_requirements_id),
	FOREIGN KEY("PrivacyBreach_id") REFERENCES "PrivacyBreach" (id),
	FOREIGN KEY(violated_requirements_id) REFERENCES "PrivacySafeguardingRequirement" (id)
);
CREATE INDEX "ix_PrivacyBreach_violated_requirements_violated_requirements_id" ON "PrivacyBreach_violated_requirements" (violated_requirements_id);
CREATE INDEX "ix_PrivacyBreach_violated_requirements_PrivacyBreach_id" ON "PrivacyBreach_violated_requirements" ("PrivacyBreach_id");

CREATE TABLE "PrivacyBreach_immediate_actions" (
	"PrivacyBreach_id" TEXT,
	immediate_actions TEXT,
	PRIMARY KEY ("PrivacyBreach_id", immediate_actions),
	FOREIGN KEY("PrivacyBreach_id") REFERENCES "PrivacyBreach" (id)
);
CREATE INDEX "ix_PrivacyBreach_immediate_actions_immediate_actions" ON "PrivacyBreach_immediate_actions" (immediate_actions);
CREATE INDEX "ix_PrivacyBreach_immediate_actions_PrivacyBreach_id" ON "PrivacyBreach_immediate_actions" ("PrivacyBreach_id");

CREATE TABLE "PrivacyBreach_notifications_made" (
	"PrivacyBreach_id" TEXT,
	notifications_made TEXT,
	PRIMARY KEY ("PrivacyBreach_id", notifications_made),
	FOREIGN KEY("PrivacyBreach_id") REFERENCES "PrivacyBreach" (id)
);
CREATE INDEX "ix_PrivacyBreach_notifications_made_PrivacyBreach_id" ON "PrivacyBreach_notifications_made" ("PrivacyBreach_id");
CREATE INDEX "ix_PrivacyBreach_notifications_made_notifications_made" ON "PrivacyBreach_notifications_made" (notifications_made);

CREATE TABLE "PrivacyBreach_remediation_actions" (
	"PrivacyBreach_id" TEXT,
	remediation_actions TEXT,
	PRIMARY KEY ("PrivacyBreach_id", remediation_actions),
	FOREIGN KEY("PrivacyBreach_id") REFERENCES "PrivacyBreach" (id)
);
CREATE INDEX "ix_PrivacyBreach_remediation_actions_PrivacyBreach_id" ON "PrivacyBreach_remediation_actions" ("PrivacyBreach_id");
CREATE INDEX "ix_PrivacyBreach_remediation_actions_remediation_actions" ON "PrivacyBreach_remediation_actions" (remediation_actions);

CREATE TABLE "PrivacyPrincipleImplementation_implementation_measures" (
	"PrivacyPrincipleImplementation_id" TEXT,
	implementation_measures TEXT,
	PRIMARY KEY ("PrivacyPrincipleImplementation_id", implementation_measures),
	FOREIGN KEY("PrivacyPrincipleImplementation_id") REFERENCES "PrivacyPrincipleImplementation" (id)
);
CREATE INDEX "ix_PrivacyPrincipleImplementation_implementation_measures_PrivacyPrincipleImplementation_id" ON "PrivacyPrincipleImplementation_implementation_measures" ("PrivacyPrincipleImplementation_id");
CREATE INDEX "ix_PrivacyPrincipleImplementation_implementation_measures_implementation_measures" ON "PrivacyPrincipleImplementation_implementation_measures" (implementation_measures);

CREATE TABLE "PrivacyPrincipleImplementation_applicable_controls_ref" (
	"PrivacyPrincipleImplementation_id" TEXT,
	applicable_controls_ref_id TEXT,
	PRIMARY KEY ("PrivacyPrincipleImplementation_id", applicable_controls_ref_id),
	FOREIGN KEY("PrivacyPrincipleImplementation_id") REFERENCES "PrivacyPrincipleImplementation" (id),
	FOREIGN KEY(applicable_controls_ref_id) REFERENCES "PrivacyControl" (id)
);
CREATE INDEX "ix_PrivacyPrincipleImplementation_applicable_controls_ref_applicable_controls_ref_id" ON "PrivacyPrincipleImplementation_applicable_controls_ref" (applicable_controls_ref_id);
CREATE INDEX "ix_PrivacyPrincipleImplementation_applicable_controls_ref_PrivacyPrincipleImplementation_id" ON "PrivacyPrincipleImplementation_applicable_controls_ref" ("PrivacyPrincipleImplementation_id");

CREATE TABLE "PrivacyPrincipleImplementation_evidence_of_adherence" (
	"PrivacyPrincipleImplementation_id" TEXT,
	evidence_of_adherence TEXT,
	PRIMARY KEY ("PrivacyPrincipleImplementation_id", evidence_of_adherence),
	FOREIGN KEY("PrivacyPrincipleImplementation_id") REFERENCES "PrivacyPrincipleImplementation" (id)
);
CREATE INDEX "ix_PrivacyPrincipleImplementation_evidence_of_adherence_evidence_of_adherence" ON "PrivacyPrincipleImplementation_evidence_of_adherence" (evidence_of_adherence);
CREATE INDEX "ix_PrivacyPrincipleImplementation_evidence_of_adherence_PrivacyPrincipleImplementation_id" ON "PrivacyPrincipleImplementation_evidence_of_adherence" ("PrivacyPrincipleImplementation_id");

CREATE TABLE "PrivacyPrincipleImplementation_gaps_identified" (
	"PrivacyPrincipleImplementation_id" TEXT,
	gaps_identified TEXT,
	PRIMARY KEY ("PrivacyPrincipleImplementation_id", gaps_identified),
	FOREIGN KEY("PrivacyPrincipleImplementation_id") REFERENCES "PrivacyPrincipleImplementation" (id)
);
CREATE INDEX "ix_PrivacyPrincipleImplementation_gaps_identified_gaps_identified" ON "PrivacyPrincipleImplementation_gaps_identified" (gaps_identified);
CREATE INDEX "ix_PrivacyPrincipleImplementation_gaps_identified_PrivacyPrincipleImplementation_id" ON "PrivacyPrincipleImplementation_gaps_identified" ("PrivacyPrincipleImplementation_id");

CREATE TABLE "PrivacyPrincipleImplementation_improvement_actions" (
	"PrivacyPrincipleImplementation_id" TEXT,
	improvement_actions TEXT,
	PRIMARY KEY ("PrivacyPrincipleImplementation_id", improvement_actions),
	FOREIGN KEY("PrivacyPrincipleImplementation_id") REFERENCES "PrivacyPrincipleImplementation" (id)
);
CREATE INDEX "ix_PrivacyPrincipleImplementation_improvement_actions_PrivacyPrincipleImplementation_id" ON "PrivacyPrincipleImplementation_improvement_actions" ("PrivacyPrincipleImplementation_id");
CREATE INDEX "ix_PrivacyPrincipleImplementation_improvement_actions_improvement_actions" ON "PrivacyPrincipleImplementation_improvement_actions" (improvement_actions);

CREATE TABLE "PIIProcessingActivity" (
	processing_purpose TEXT,
	legal_basis TEXT,
	controller_ref TEXT,
	processor_ref TEXT,
	retention_period TEXT,
	cross_border_transfer BOOLEAN,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	created_date DATE,
	modified_date DATE,
	"PrivacyFramework_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(controller_ref) REFERENCES "PIIController" (id),
	FOREIGN KEY(processor_ref) REFERENCES "PIIProcessor" (id),
	FOREIGN KEY("PrivacyFramework_id") REFERENCES "PrivacyFramework" (id)
);
CREATE INDEX "ix_PIIProcessingActivity_id" ON "PIIProcessingActivity" (id);

CREATE TABLE "PIIController_appointed_processors" (
	"PIIController_id" TEXT,
	appointed_processors_id TEXT,
	PRIMARY KEY ("PIIController_id", appointed_processors_id),
	FOREIGN KEY("PIIController_id") REFERENCES "PIIController" (id),
	FOREIGN KEY(appointed_processors_id) REFERENCES "PIIProcessor" (id)
);
CREATE INDEX "ix_PIIController_appointed_processors_appointed_processors_id" ON "PIIController_appointed_processors" (appointed_processors_id);
CREATE INDEX "ix_PIIController_appointed_processors_PIIController_id" ON "PIIController_appointed_processors" ("PIIController_id");

CREATE TABLE "PIIProcessor_sub_processors" (
	"PIIProcessor_id" TEXT,
	sub_processors_id TEXT,
	PRIMARY KEY ("PIIProcessor_id", sub_processors_id),
	FOREIGN KEY("PIIProcessor_id") REFERENCES "PIIProcessor" (id),
	FOREIGN KEY(sub_processors_id) REFERENCES "PIIProcessor" (id)
);
CREATE INDEX "ix_PIIProcessor_sub_processors_PIIProcessor_id" ON "PIIProcessor_sub_processors" ("PIIProcessor_id");
CREATE INDEX "ix_PIIProcessor_sub_processors_sub_processors_id" ON "PIIProcessor_sub_processors" (sub_processors_id);

CREATE TABLE "PIIProcessor_jurisdictions" (
	"PIIProcessor_id" TEXT,
	jurisdictions TEXT,
	PRIMARY KEY ("PIIProcessor_id", jurisdictions),
	FOREIGN KEY("PIIProcessor_id") REFERENCES "PIIProcessor" (id)
);
CREATE INDEX "ix_PIIProcessor_jurisdictions_PIIProcessor_id" ON "PIIProcessor_jurisdictions" ("PIIProcessor_id");
CREATE INDEX "ix_PIIProcessor_jurisdictions_jurisdictions" ON "PIIProcessor_jurisdictions" (jurisdictions);

CREATE TABLE "PrivacyImpactAssessment_processing_activities_assessed" (
	"PrivacyImpactAssessment_id" TEXT,
	processing_activities_assessed_id TEXT,
	PRIMARY KEY ("PrivacyImpactAssessment_id", processing_activities_assessed_id),
	FOREIGN KEY("PrivacyImpactAssessment_id") REFERENCES "PrivacyImpactAssessment" (id),
	FOREIGN KEY(processing_activities_assessed_id) REFERENCES "PIIProcessingActivity" (id)
);
CREATE INDEX "ix_PrivacyImpactAssessment_processing_activities_assessed_PrivacyImpactAssessment_id" ON "PrivacyImpactAssessment_processing_activities_assessed" ("PrivacyImpactAssessment_id");
CREATE INDEX "ix_PrivacyImpactAssessment_processing_activities_assessed_processing_activities_assessed_id" ON "PrivacyImpactAssessment_processing_activities_assessed" (processing_activities_assessed_id);

CREATE TABLE "PIIProcessingActivity_operations_performed" (
	"PIIProcessingActivity_id" TEXT,
	operations_performed VARCHAR(16),
	PRIMARY KEY ("PIIProcessingActivity_id", operations_performed),
	FOREIGN KEY("PIIProcessingActivity_id") REFERENCES "PIIProcessingActivity" (id)
);
CREATE INDEX "ix_PIIProcessingActivity_operations_performed_operations_performed" ON "PIIProcessingActivity_operations_performed" (operations_performed);
CREATE INDEX "ix_PIIProcessingActivity_operations_performed_PIIProcessingActivity_id" ON "PIIProcessingActivity_operations_performed" ("PIIProcessingActivity_id");

CREATE TABLE "PIIProcessingActivity_pii_categories_processed" (
	"PIIProcessingActivity_id" TEXT,
	pii_categories_processed TEXT,
	PRIMARY KEY ("PIIProcessingActivity_id", pii_categories_processed),
	FOREIGN KEY("PIIProcessingActivity_id") REFERENCES "PIIProcessingActivity" (id)
);
CREATE INDEX "ix_PIIProcessingActivity_pii_categories_processed_pii_categories_processed" ON "PIIProcessingActivity_pii_categories_processed" (pii_categories_processed);
CREATE INDEX "ix_PIIProcessingActivity_pii_categories_processed_PIIProcessingActivity_id" ON "PIIProcessingActivity_pii_categories_processed" ("PIIProcessingActivity_id");

CREATE TABLE "PIIProcessingActivity_sensitivity_levels_involved" (
	"PIIProcessingActivity_id" TEXT,
	sensitivity_levels_involved VARCHAR(9),
	PRIMARY KEY ("PIIProcessingActivity_id", sensitivity_levels_involved),
	FOREIGN KEY("PIIProcessingActivity_id") REFERENCES "PIIProcessingActivity" (id)
);
CREATE INDEX "ix_PIIProcessingActivity_sensitivity_levels_involved_PIIProcessingActivity_id" ON "PIIProcessingActivity_sensitivity_levels_involved" ("PIIProcessingActivity_id");
CREATE INDEX "ix_PIIProcessingActivity_sensitivity_levels_involved_sensitivity_levels_involved" ON "PIIProcessingActivity_sensitivity_levels_involved" (sensitivity_levels_involved);

CREATE TABLE "PIIProcessingActivity_data_flows" (
	"PIIProcessingActivity_id" TEXT,
	data_flows_id TEXT,
	PRIMARY KEY ("PIIProcessingActivity_id", data_flows_id),
	FOREIGN KEY("PIIProcessingActivity_id") REFERENCES "PIIProcessingActivity" (id),
	FOREIGN KEY(data_flows_id) REFERENCES "PIIFlowScenario" (id)
);
CREATE INDEX "ix_PIIProcessingActivity_data_flows_PIIProcessingActivity_id" ON "PIIProcessingActivity_data_flows" ("PIIProcessingActivity_id");
CREATE INDEX "ix_PIIProcessingActivity_data_flows_data_flows_id" ON "PIIProcessingActivity_data_flows" (data_flows_id);

CREATE TABLE "PIIProcessingActivity_privacy_controls_applied" (
	"PIIProcessingActivity_id" TEXT,
	privacy_controls_applied_id TEXT,
	PRIMARY KEY ("PIIProcessingActivity_id", privacy_controls_applied_id),
	FOREIGN KEY("PIIProcessingActivity_id") REFERENCES "PIIProcessingActivity" (id),
	FOREIGN KEY(privacy_controls_applied_id) REFERENCES "PrivacyControl" (id)
);
CREATE INDEX "ix_PIIProcessingActivity_privacy_controls_applied_privacy_controls_applied_id" ON "PIIProcessingActivity_privacy_controls_applied" (privacy_controls_applied_id);
CREATE INDEX "ix_PIIProcessingActivity_privacy_controls_applied_PIIProcessingActivity_id" ON "PIIProcessingActivity_privacy_controls_applied" ("PIIProcessingActivity_id");

CREATE TABLE "PIIProcessingActivity_transfer_safeguards" (
	"PIIProcessingActivity_id" TEXT,
	transfer_safeguards TEXT,
	PRIMARY KEY ("PIIProcessingActivity_id", transfer_safeguards),
	FOREIGN KEY("PIIProcessingActivity_id") REFERENCES "PIIProcessingActivity" (id)
);
CREATE INDEX "ix_PIIProcessingActivity_transfer_safeguards_PIIProcessingActivity_id" ON "PIIProcessingActivity_transfer_safeguards" ("PIIProcessingActivity_id");
CREATE INDEX "ix_PIIProcessingActivity_transfer_safeguards_transfer_safeguards" ON "PIIProcessingActivity_transfer_safeguards" (transfer_safeguards);
