-- # Class: PfRecordMixin Description: What every record of the framework has, so that other records can refer to it: an identifier, a title and a description.
--     * Slot: pf_id Description: The record's identifier, unique among the records of the framework, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
-- # Class: PfFramework Description: One organization's use of the privacy framework: the systems it covers, and every record the organization keeps about them, each kind in a list of its own.
--     * Slot: pf_organization Description: The organization that applies the framework.
--     * Slot: pf_id Description: The record's identifier, unique among the records of the framework, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
-- # Abstract Class: PfActor Description: Someone who takes part in handling PII, told apart by the part they play. One party can play different parts for different PII, with a record for each.
--     * Slot: pf_actor_type Description: The kind of actor: PfPiiPrincipal, PfPiiController, PfPiiProcessor or PfThirdParty.
--     * Slot: pf_contact Description: How to reach the actor about privacy.
--     * Slot: pf_id Description: The record's identifier, unique among the records of the framework, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
--     * Slot: PfFramework_pf_id Description: Autocreated FK slot
-- # Class: PfPiiPrincipal Description: The person the PII is about, or a group of such people when the organization records them together.
--     * Slot: pf_actor_type Description: The kind of actor: PfPiiPrincipal, PfPiiController, PfPiiProcessor or PfThirdParty.
--     * Slot: pf_contact Description: How to reach the actor about privacy.
--     * Slot: pf_id Description: The record's identifier, unique among the records of the framework, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
-- # Class: PfPiiController Description: The party that decides why and how PII is processed, and answers for it even when another party does the work.
--     * Slot: pf_controller_policy Description: The privacy policy the controller works under.
--     * Slot: pf_privacy_officer Description: The person who advises the controller on privacy, where there is one.
--     * Slot: pf_actor_type Description: The kind of actor: PfPiiPrincipal, PfPiiController, PfPiiProcessor or PfThirdParty.
--     * Slot: pf_contact Description: How to reach the actor about privacy.
--     * Slot: pf_id Description: The record's identifier, unique among the records of the framework, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
-- # Class: PfPiiProcessor Description: A party that processes PII for a controller, on that controller's instructions.
--     * Slot: pf_processing_agreement Description: The reference of the agreement that binds the processor, where there is one.
--     * Slot: pf_actor_type Description: The kind of actor: PfPiiPrincipal, PfPiiController, PfPiiProcessor or PfThirdParty.
--     * Slot: pf_contact Description: How to reach the actor about privacy.
--     * Slot: pf_id Description: The record's identifier, unique among the records of the framework, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
-- # Class: PfThirdParty Description: A party outside the controller and its processors that receives PII for its own ends, and usually becomes a controller of that PII.
--     * Slot: pf_receiving_purpose Description: What the third party receives the PII for.
--     * Slot: pf_transfer_basis Description: What makes the passing of PII to the third party lawful.
--     * Slot: pf_actor_type Description: The kind of actor: PfPiiPrincipal, PfPiiController, PfPiiProcessor or PfThirdParty.
--     * Slot: pf_contact Description: How to reach the actor about privacy.
--     * Slot: pf_id Description: The record's identifier, unique among the records of the framework, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
-- # Class: PfPiiItem Description: A piece or set of information that can be tied to a person, why it counts as PII, how sensitive it is and how it is handled.
--     * Slot: pf_retention Description: How long the PII is kept, as an ISO 8601 duration.
--     * Slot: pf_sensitivity Description: How sensitive the item is.
--     * Slot: pf_pseudonymized Description: Whether an alias stands in for the item's identifying details.
--     * Slot: pf_linkability Description: How easily the item could be joined with other data to identify someone, in the organization's words.
--     * Slot: pf_id Description: The record's identifier, unique among the records of the framework, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
--     * Slot: PfFramework_pf_id Description: Autocreated FK slot
-- # Class: PfPiiFlow Description: One way PII passes from one actor to another, and who decides what happens to it afterwards.
--     * Slot: pf_provider Description: The actor the PII comes from.
--     * Slot: pf_recipient Description: The actor the PII goes to.
--     * Slot: pf_decides_afterwards Description: The actor that decides what happens to the PII once it has passed. A processor never holds this position.
--     * Slot: pf_id Description: The record's identifier, unique among the records of the framework, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
--     * Slot: PfFramework_pf_id Description: Autocreated FK slot
-- # Class: PfProcessingActivity Description: Something the organization does with PII: why, on what basis, what it does to which PII, who is responsible, and how long the PII is kept.
--     * Slot: pf_retention Description: How long the PII is kept, as an ISO 8601 duration.
--     * Slot: pf_controller Description: The controller that answers for the activity.
--     * Slot: pf_crosses_borders Description: Whether PII leaves the jurisdiction it was collected in.
--     * Slot: pf_id Description: The record's identifier, unique among the records of the framework, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
--     * Slot: PfFramework_pf_id Description: Autocreated FK slot
-- # Class: PfSafeguardingRequirement Description: Something the organization must do to protect PII, and where that duty comes from.
--     * Slot: pf_requirement_factor Description: Where the requirement comes from.
--     * Slot: pf_requirement_source Description: The law, contract or other document that states it.
--     * Slot: pf_id Description: The record's identifier, unique among the records of the framework, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
--     * Slot: PfFramework_pf_id Description: Autocreated FK slot
-- # Class: PfPolicy Description: A privacy policy: what the organization commits to about PII, written for its own people or as a notice to the people whose PII it handles.
--     * Slot: pf_policy_audience Description: Who the policy is written for.
--     * Slot: pf_policy_version Description: The version of the policy.
--     * Slot: pf_policy_scope Description: What the policy covers.
--     * Slot: pf_policy_effective_date Description: When the policy takes effect.
--     * Slot: pf_policy_last_reviewed Description: When the policy was last reviewed.
--     * Slot: pf_retention_statement Description: What the policy says about how long PII is kept.
--     * Slot: pf_inquiry_contact Description: Where people can send questions about the policy.
--     * Slot: pf_id Description: The record's identifier, unique among the records of the framework, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
--     * Slot: PfFramework_pf_id Description: Autocreated FK slot
-- # Class: PfControl Description: A measure that treats a privacy risk by making it less likely or less harmful, the principles it serves and how far it has been put into effect.
--     * Slot: pf_control_kind Description: The form the control takes.
--     * Slot: pf_control_objective Description: What the control is meant to achieve.
--     * Slot: pf_control_detail Description: How the control is put into effect.
--     * Slot: pf_control_responsible Description: The actor that answers for the control.
--     * Slot: pf_control_state Description: How far the control has been put into effect.
--     * Slot: pf_id Description: The record's identifier, unique among the records of the framework, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
--     * Slot: PfFramework_pf_id Description: Autocreated FK slot
-- # Class: PfPrincipleImplementation Description: How the organization stands against one privacy principle: what it does, what shows it, and what is still missing.
--     * Slot: pf_principle Description: The principle the record is about.
--     * Slot: pf_last_assessed Description: When the organization last checked its standing.
--     * Slot: pf_id Description: The record's identifier, unique among the records of the framework, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
--     * Slot: PfFramework_pf_id Description: Autocreated FK slot
-- # Class: PfRisk Description: A way that handling PII could harm people: where the risk comes from, how likely and how bad it is, and what is done about it.
--     * Slot: pf_risk_source Description: Where the risk comes from.
--     * Slot: pf_risk_likelihood Description: How likely the harm is, in the organization's own terms.
--     * Slot: pf_risk_consequence Description: What the harm to people would be.
--     * Slot: pf_risk_inherent_level Description: The risk's level before controls.
--     * Slot: pf_risk_residual_level Description: The risk's level after controls, which is never above the level before.
--     * Slot: pf_risk_owner Description: The person who answers for the risk.
--     * Slot: pf_id Description: The record's identifier, unique among the records of the framework, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
--     * Slot: PfFramework_pf_id Description: Autocreated FK slot
-- # Class: PfImpactAssessment Description: A review of what a system or activity could do to people's privacy, the risks it found and what became of them.
--     * Slot: pf_assessment_scope Description: What the assessment looks at.
--     * Slot: pf_assessment_date Description: When the assessment was done.
--     * Slot: pf_assessor Description: Who did the assessment.
--     * Slot: pf_assessment_outcome Description: What the assessment concluded.
--     * Slot: pf_next_assessment Description: When the next assessment is due, which is after this one.
--     * Slot: pf_id Description: The record's identifier, unique among the records of the framework, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
--     * Slot: PfFramework_pf_id Description: Autocreated FK slot
-- # Class: PfBreach Description: A time when PII was handled against a safeguarding requirement: what happened, who was told and what was done.
--     * Slot: pf_breach_occurred Description: When the breach happened.
--     * Slot: pf_breach_discovered Description: When the organization found out, which is not before it happened.
--     * Slot: pf_breach_closed Description: When the organization closed the matter, which is not before it found out.
--     * Slot: pf_principals_affected Description: How many people the breach reached, where that is known.
--     * Slot: pf_breach_severity Description: How serious the breach is.
--     * Slot: pf_notification_required Description: Whether a law or contract requires anyone to be told.
--     * Slot: pf_lessons Description: What the organization learned.
--     * Slot: pf_id Description: The record's identifier, unique among the records of the framework, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
--     * Slot: PfFramework_pf_id Description: Autocreated FK slot
-- # Class: PfConsent Description: One person's agreement to the processing of their PII for stated purposes, and where it stands.
--     * Slot: pf_principal Description: The person the record is about.
--     * Slot: pf_consent_mechanism Description: How the agreement was obtained.
--     * Slot: pf_consent_given Description: When the person agreed.
--     * Slot: pf_consent_state Description: Where the agreement stands.
--     * Slot: pf_consent_withdrawn Description: When the person took the agreement back.
--     * Slot: pf_id Description: The record's identifier, unique among the records of the framework, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
--     * Slot: PfFramework_pf_id Description: Autocreated FK slot
-- # Class: PfPreference Description: What one person has said they want done, or not done, with their PII.
--     * Slot: pf_principal Description: The person the record is about.
--     * Slot: pf_preference_scope Description: What the preference applies to.
--     * Slot: pf_wants_anonymity Description: Whether the person asks not to be identified at all.
--     * Slot: pf_wants_pseudonymity Description: Whether the person asks to appear under an alias.
--     * Slot: pf_preference_recorded Description: When the organization recorded the preference.
--     * Slot: pf_id Description: The record's identifier, unique among the records of the framework, such as a URI or a CURIE. Other records refer to the record by it.
--     * Slot: title Description: The name the organization gives the record.
--     * Slot: description Description: What the record says or describes, in the organization's own words.
--     * Slot: PfFramework_pf_id Description: Autocreated FK slot
-- # Class: PfFramework_pf_jurisdictions
--     * Slot: PfFramework_pf_id Description: Autocreated FK slot
--     * Slot: pf_jurisdictions Description: The legal systems that apply to the record, in the organization's terms.
-- # Class: PfFramework_pf_ict_systems
--     * Slot: PfFramework_pf_id Description: Autocreated FK slot
--     * Slot: pf_ict_systems Description: The ICT systems the framework covers.
-- # Class: PfActor_pf_jurisdictions
--     * Slot: PfActor_pf_id Description: Autocreated FK slot
--     * Slot: pf_jurisdictions Description: The legal systems that apply to the record, in the organization's terms.
-- # Class: PfPiiPrincipal_pf_jurisdictions
--     * Slot: PfPiiPrincipal_pf_id Description: Autocreated FK slot
--     * Slot: pf_jurisdictions Description: The legal systems that apply to the record, in the organization's terms.
-- # Class: PfPiiController_pf_purposes
--     * Slot: PfPiiController_pf_id Description: Autocreated FK slot
--     * Slot: pf_purposes Description: The reasons the PII is processed, in the organization's own words.
-- # Class: PfPiiController_pf_legal_bases
--     * Slot: PfPiiController_pf_id Description: Autocreated FK slot
--     * Slot: pf_legal_bases Description: What makes the processing lawful, in the terms of the law that applies.
-- # Class: PfPiiController_pf_appointed_processors
--     * Slot: PfPiiController_pf_id Description: Autocreated FK slot
--     * Slot: pf_appointed_processors_pf_id Description: The processors that work for the controller.
-- # Class: PfPiiController_pf_jurisdictions
--     * Slot: PfPiiController_pf_id Description: Autocreated FK slot
--     * Slot: pf_jurisdictions Description: The legal systems that apply to the record, in the organization's terms.
-- # Class: PfPiiProcessor_pf_instructing_controllers
--     * Slot: PfPiiProcessor_pf_id Description: Autocreated FK slot
--     * Slot: pf_instructing_controllers_pf_id Description: The controllers whose instructions the processor follows.
-- # Class: PfPiiProcessor_pf_sub_processors
--     * Slot: PfPiiProcessor_pf_id Description: Autocreated FK slot
--     * Slot: pf_sub_processors_pf_id Description: The processors this processor has engaged in turn.
-- # Class: PfPiiProcessor_pf_jurisdictions
--     * Slot: PfPiiProcessor_pf_id Description: Autocreated FK slot
--     * Slot: pf_jurisdictions Description: The legal systems that apply to the record, in the organization's terms.
-- # Class: PfThirdParty_pf_jurisdictions
--     * Slot: PfThirdParty_pf_id Description: Autocreated FK slot
--     * Slot: pf_jurisdictions Description: The legal systems that apply to the record, in the organization's terms.
-- # Class: PfPiiItem_pf_concerned_principals
--     * Slot: PfPiiItem_pf_id Description: Autocreated FK slot
--     * Slot: pf_concerned_principals_pf_id Description: The people the PII of the record is about.
-- # Class: PfPiiItem_pf_operations
--     * Slot: PfPiiItem_pf_id Description: Autocreated FK slot
--     * Slot: pf_operations Description: The things done to the PII.
-- # Class: PfPiiItem_pf_pii_categories
--     * Slot: PfPiiItem_pf_id Description: Autocreated FK slot
--     * Slot: pf_pii_categories Description: What the item holds, in the organization's own words.
-- # Class: PfPiiItem_pf_recognized_by
--     * Slot: PfPiiItem_pf_id Description: Autocreated FK slot
--     * Slot: pf_recognized_by Description: Why the information counts as PII.
-- # Class: PfPiiFlow_pf_concerned_pii
--     * Slot: PfPiiFlow_pf_id Description: Autocreated FK slot
--     * Slot: pf_concerned_pii_pf_id Description: The PII items the record concerns.
-- # Class: PfProcessingActivity_pf_purposes
--     * Slot: PfProcessingActivity_pf_id Description: Autocreated FK slot
--     * Slot: pf_purposes Description: The reasons the PII is processed, in the organization's own words.
-- # Class: PfProcessingActivity_pf_legal_bases
--     * Slot: PfProcessingActivity_pf_id Description: Autocreated FK slot
--     * Slot: pf_legal_bases Description: What makes the processing lawful, in the terms of the law that applies.
-- # Class: PfProcessingActivity_pf_operations
--     * Slot: PfProcessingActivity_pf_id Description: Autocreated FK slot
--     * Slot: pf_operations Description: The things done to the PII.
-- # Class: PfProcessingActivity_pf_concerned_pii
--     * Slot: PfProcessingActivity_pf_id Description: Autocreated FK slot
--     * Slot: pf_concerned_pii_pf_id Description: The PII items the record concerns.
-- # Class: PfProcessingActivity_pf_related_controls
--     * Slot: PfProcessingActivity_pf_id Description: Autocreated FK slot
--     * Slot: pf_related_controls_pf_id Description: The organization's controls that act on the record's subject.
-- # Class: PfProcessingActivity_pf_processors
--     * Slot: PfProcessingActivity_pf_id Description: Autocreated FK slot
--     * Slot: pf_processors_pf_id Description: The processors that do the work.
-- # Class: PfProcessingActivity_pf_activity_flows
--     * Slot: PfProcessingActivity_pf_id Description: Autocreated FK slot
--     * Slot: pf_activity_flows_pf_id Description: The flows of PII the activity involves.
-- # Class: PfProcessingActivity_pf_sensitivities
--     * Slot: PfProcessingActivity_pf_id Description: Autocreated FK slot
--     * Slot: pf_sensitivities Description: The levels of sensitivity among the PII involved.
-- # Class: PfProcessingActivity_pf_transfer_safeguards
--     * Slot: PfProcessingActivity_pf_id Description: Autocreated FK slot
--     * Slot: pf_transfer_safeguards Description: What protects the PII when it crosses a border.
-- # Class: PfSafeguardingRequirement_pf_applies_to
--     * Slot: PfSafeguardingRequirement_pf_id Description: Autocreated FK slot
--     * Slot: pf_applies_to_pf_id Description: The actors that must meet it.
-- # Class: PfSafeguardingRequirement_pf_met_by
--     * Slot: PfSafeguardingRequirement_pf_id Description: Autocreated FK slot
--     * Slot: pf_met_by_pf_id Description: The controls that meet it.
-- # Class: PfPolicy_pf_purposes
--     * Slot: PfPolicy_pf_id Description: Autocreated FK slot
--     * Slot: pf_purposes Description: The reasons the PII is processed, in the organization's own words.
-- # Class: PfPolicy_pf_concerned_pii
--     * Slot: PfPolicy_pf_id Description: Autocreated FK slot
--     * Slot: pf_concerned_pii_pf_id Description: The PII items the record concerns.
-- # Class: PfPolicy_pf_principles
--     * Slot: PfPolicy_pf_id Description: Autocreated FK slot
--     * Slot: pf_principles Description: The privacy principles the record bears on.
-- # Class: PfPolicy_pf_stated_rights
--     * Slot: PfPolicy_pf_id Description: Autocreated FK slot
--     * Slot: pf_stated_rights Description: The rights the policy tells people they have.
-- # Class: PfControl_pf_principles
--     * Slot: PfControl_pf_id Description: Autocreated FK slot
--     * Slot: pf_principles Description: The privacy principles the record bears on.
-- # Class: PfControl_pf_evidence
--     * Slot: PfControl_pf_id Description: Autocreated FK slot
--     * Slot: pf_evidence Description: What shows that the record's claim holds, such as a report or a log.
-- # Class: PfControl_pf_answers_requirements
--     * Slot: PfControl_pf_id Description: Autocreated FK slot
--     * Slot: pf_answers_requirements_pf_id Description: The safeguarding requirements the control answers to.
-- # Class: PfPrincipleImplementation_pf_related_controls
--     * Slot: PfPrincipleImplementation_pf_id Description: Autocreated FK slot
--     * Slot: pf_related_controls_pf_id Description: The organization's controls that act on the record's subject.
-- # Class: PfPrincipleImplementation_pf_evidence
--     * Slot: PfPrincipleImplementation_pf_id Description: Autocreated FK slot
--     * Slot: pf_evidence Description: What shows that the record's claim holds, such as a report or a log.
-- # Class: PfPrincipleImplementation_pf_measures
--     * Slot: PfPrincipleImplementation_pf_id Description: Autocreated FK slot
--     * Slot: pf_measures Description: What the organization does to follow the principle.
-- # Class: PfPrincipleImplementation_pf_gaps
--     * Slot: PfPrincipleImplementation_pf_id Description: Autocreated FK slot
--     * Slot: pf_gaps Description: Where the organization falls short.
-- # Class: PfPrincipleImplementation_pf_improvements
--     * Slot: PfPrincipleImplementation_pf_id Description: Autocreated FK slot
--     * Slot: pf_improvements Description: What the organization will do about the gaps.
-- # Class: PfRisk_pf_concerned_pii
--     * Slot: PfRisk_pf_id Description: Autocreated FK slot
--     * Slot: pf_concerned_pii_pf_id Description: The PII items the record concerns.
-- # Class: PfRisk_pf_concerned_principals
--     * Slot: PfRisk_pf_id Description: Autocreated FK slot
--     * Slot: pf_concerned_principals_pf_id Description: The people the PII of the record is about.
-- # Class: PfRisk_pf_related_controls
--     * Slot: PfRisk_pf_id Description: Autocreated FK slot
--     * Slot: pf_related_controls_pf_id Description: The organization's controls that act on the record's subject.
-- # Class: PfImpactAssessment_pf_assessed_activities
--     * Slot: PfImpactAssessment_pf_id Description: Autocreated FK slot
--     * Slot: pf_assessed_activities_pf_id Description: The processing activities it looks at.
-- # Class: PfImpactAssessment_pf_risks_found
--     * Slot: PfImpactAssessment_pf_id Description: Autocreated FK slot
--     * Slot: pf_risks_found_pf_id Description: The risks it found.
-- # Class: PfImpactAssessment_pf_risks_treated
--     * Slot: PfImpactAssessment_pf_id Description: Autocreated FK slot
--     * Slot: pf_risks_treated_pf_id Description: Those of the risks found that have been treated.
-- # Class: PfImpactAssessment_pf_risks_accepted
--     * Slot: PfImpactAssessment_pf_id Description: Autocreated FK slot
--     * Slot: pf_risks_accepted_pf_id Description: Those of the risks found that the organization has accepted as they stand.
-- # Class: PfImpactAssessment_pf_consultations
--     * Slot: PfImpactAssessment_pf_id Description: Autocreated FK slot
--     * Slot: pf_consultations Description: Who was asked, and what they said.
-- # Class: PfBreach_pf_concerned_pii
--     * Slot: PfBreach_pf_id Description: Autocreated FK slot
--     * Slot: pf_concerned_pii_pf_id Description: The PII items the record concerns.
-- # Class: PfBreach_pf_breached_requirements
--     * Slot: PfBreach_pf_id Description: Autocreated FK slot
--     * Slot: pf_breached_requirements_pf_id Description: The safeguarding requirements the breach went against.
-- # Class: PfBreach_pf_immediate_actions
--     * Slot: PfBreach_pf_id Description: Autocreated FK slot
--     * Slot: pf_immediate_actions Description: What was done straight away.
-- # Class: PfBreach_pf_notifications
--     * Slot: PfBreach_pf_id Description: Autocreated FK slot
--     * Slot: pf_notifications Description: Who was told, and when.
-- # Class: PfBreach_pf_remediation
--     * Slot: PfBreach_pf_id Description: Autocreated FK slot
--     * Slot: pf_remediation Description: What was done to put things right.
-- # Class: PfConsent_pf_purposes
--     * Slot: PfConsent_pf_id Description: Autocreated FK slot
--     * Slot: pf_purposes Description: The reasons the PII is processed, in the organization's own words.
-- # Class: PfConsent_pf_concerned_pii
--     * Slot: PfConsent_pf_id Description: Autocreated FK slot
--     * Slot: pf_concerned_pii_pf_id Description: The PII items the record concerns.
-- # Class: PfConsent_pf_evidence
--     * Slot: PfConsent_pf_id Description: Autocreated FK slot
--     * Slot: pf_evidence Description: What shows that the record's claim holds, such as a report or a log.
-- # Class: PfPreference_pf_refused_operations
--     * Slot: PfPreference_pf_id Description: Autocreated FK slot
--     * Slot: pf_refused_operations Description: What the person does not want done to their PII.
-- # Class: PfPreference_pf_refused_recipients
--     * Slot: PfPreference_pf_id Description: Autocreated FK slot
--     * Slot: pf_refused_recipients Description: Who the person does not want their PII passed to.

CREATE TABLE "PfRecordMixin" (
	pf_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (pf_id)
);
CREATE INDEX "ix_PfRecordMixin_pf_id" ON "PfRecordMixin" (pf_id);

CREATE TABLE "PfFramework" (
	pf_organization TEXT NOT NULL,
	pf_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (pf_id)
);
CREATE INDEX "ix_PfFramework_pf_id" ON "PfFramework" (pf_id);

CREATE TABLE "PfPiiPrincipal" (
	pf_actor_type TEXT NOT NULL,
	pf_contact TEXT,
	pf_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (pf_id)
);
CREATE INDEX "ix_PfPiiPrincipal_pf_id" ON "PfPiiPrincipal" (pf_id);

CREATE TABLE "PfPiiProcessor" (
	pf_processing_agreement TEXT,
	pf_actor_type TEXT NOT NULL,
	pf_contact TEXT,
	pf_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (pf_id)
);
CREATE INDEX "ix_PfPiiProcessor_pf_id" ON "PfPiiProcessor" (pf_id);

CREATE TABLE "PfThirdParty" (
	pf_receiving_purpose TEXT,
	pf_transfer_basis TEXT,
	pf_actor_type TEXT NOT NULL,
	pf_contact TEXT,
	pf_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (pf_id)
);
CREATE INDEX "ix_PfThirdParty_pf_id" ON "PfThirdParty" (pf_id);

CREATE TABLE "PfActor" (
	pf_actor_type TEXT NOT NULL,
	pf_contact TEXT,
	pf_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	"PfFramework_pf_id" TEXT,
	PRIMARY KEY (pf_id),
	FOREIGN KEY("PfFramework_pf_id") REFERENCES "PfFramework" (pf_id)
);
CREATE INDEX "ix_PfActor_pf_id" ON "PfActor" (pf_id);

CREATE TABLE "PfPiiItem" (
	pf_retention TEXT,
	pf_sensitivity VARCHAR(9),
	pf_pseudonymized BOOLEAN,
	pf_linkability TEXT,
	pf_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	"PfFramework_pf_id" TEXT,
	PRIMARY KEY (pf_id),
	FOREIGN KEY("PfFramework_pf_id") REFERENCES "PfFramework" (pf_id)
);
CREATE INDEX "ix_PfPiiItem_pf_id" ON "PfPiiItem" (pf_id);

CREATE TABLE "PfSafeguardingRequirement" (
	pf_requirement_factor VARCHAR(8) NOT NULL,
	pf_requirement_source TEXT,
	pf_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	"PfFramework_pf_id" TEXT,
	PRIMARY KEY (pf_id),
	FOREIGN KEY("PfFramework_pf_id") REFERENCES "PfFramework" (pf_id)
);
CREATE INDEX "ix_PfSafeguardingRequirement_pf_id" ON "PfSafeguardingRequirement" (pf_id);

CREATE TABLE "PfPolicy" (
	pf_policy_audience VARCHAR(13) NOT NULL,
	pf_policy_version TEXT,
	pf_policy_scope TEXT,
	pf_policy_effective_date DATE,
	pf_policy_last_reviewed DATE,
	pf_retention_statement TEXT,
	pf_inquiry_contact TEXT,
	pf_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	"PfFramework_pf_id" TEXT,
	PRIMARY KEY (pf_id),
	FOREIGN KEY("PfFramework_pf_id") REFERENCES "PfFramework" (pf_id)
);
CREATE INDEX "ix_PfPolicy_pf_id" ON "PfPolicy" (pf_id);

CREATE TABLE "PfPrincipleImplementation" (
	pf_principle VARCHAR(14) NOT NULL,
	pf_last_assessed DATE,
	pf_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	"PfFramework_pf_id" TEXT,
	PRIMARY KEY (pf_id),
	FOREIGN KEY("PfFramework_pf_id") REFERENCES "PfFramework" (pf_id)
);
CREATE INDEX "ix_PfPrincipleImplementation_pf_id" ON "PfPrincipleImplementation" (pf_id);

CREATE TABLE "PfRisk" (
	pf_risk_source TEXT,
	pf_risk_likelihood TEXT,
	pf_risk_consequence TEXT,
	pf_risk_inherent_level VARCHAR(9),
	pf_risk_residual_level VARCHAR(9),
	pf_risk_owner TEXT,
	pf_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	"PfFramework_pf_id" TEXT,
	PRIMARY KEY (pf_id),
	FOREIGN KEY("PfFramework_pf_id") REFERENCES "PfFramework" (pf_id)
);
CREATE INDEX "ix_PfRisk_pf_id" ON "PfRisk" (pf_id);

CREATE TABLE "PfImpactAssessment" (
	pf_assessment_scope TEXT,
	pf_assessment_date DATE,
	pf_assessor TEXT,
	pf_assessment_outcome TEXT,
	pf_next_assessment DATE,
	pf_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	"PfFramework_pf_id" TEXT,
	PRIMARY KEY (pf_id),
	FOREIGN KEY("PfFramework_pf_id") REFERENCES "PfFramework" (pf_id)
);
CREATE INDEX "ix_PfImpactAssessment_pf_id" ON "PfImpactAssessment" (pf_id);

CREATE TABLE "PfBreach" (
	pf_breach_occurred DATETIME,
	pf_breach_discovered DATETIME,
	pf_breach_closed DATETIME,
	pf_principals_affected INTEGER,
	pf_breach_severity VARCHAR(9),
	pf_notification_required BOOLEAN,
	pf_lessons TEXT,
	pf_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	"PfFramework_pf_id" TEXT,
	PRIMARY KEY (pf_id),
	FOREIGN KEY("PfFramework_pf_id") REFERENCES "PfFramework" (pf_id)
);
CREATE INDEX "ix_PfBreach_pf_id" ON "PfBreach" (pf_id);

CREATE TABLE "PfConsent" (
	pf_principal TEXT NOT NULL,
	pf_consent_mechanism VARCHAR(7),
	pf_consent_given DATETIME,
	pf_consent_state VARCHAR(9) NOT NULL,
	pf_consent_withdrawn DATETIME,
	pf_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	"PfFramework_pf_id" TEXT,
	PRIMARY KEY (pf_id),
	FOREIGN KEY(pf_principal) REFERENCES "PfPiiPrincipal" (pf_id),
	FOREIGN KEY("PfFramework_pf_id") REFERENCES "PfFramework" (pf_id)
);
CREATE INDEX "ix_PfConsent_pf_id" ON "PfConsent" (pf_id);

CREATE TABLE "PfPreference" (
	pf_principal TEXT NOT NULL,
	pf_preference_scope TEXT,
	pf_wants_anonymity BOOLEAN,
	pf_wants_pseudonymity BOOLEAN,
	pf_preference_recorded DATE,
	pf_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	"PfFramework_pf_id" TEXT,
	PRIMARY KEY (pf_id),
	FOREIGN KEY(pf_principal) REFERENCES "PfPiiPrincipal" (pf_id),
	FOREIGN KEY("PfFramework_pf_id") REFERENCES "PfFramework" (pf_id)
);
CREATE INDEX "ix_PfPreference_pf_id" ON "PfPreference" (pf_id);

CREATE TABLE "PfFramework_pf_jurisdictions" (
	"PfFramework_pf_id" TEXT,
	pf_jurisdictions TEXT,
	PRIMARY KEY ("PfFramework_pf_id", pf_jurisdictions),
	FOREIGN KEY("PfFramework_pf_id") REFERENCES "PfFramework" (pf_id)
);
CREATE INDEX "ix_PfFramework_pf_jurisdictions_PfFramework_pf_id" ON "PfFramework_pf_jurisdictions" ("PfFramework_pf_id");
CREATE INDEX "ix_PfFramework_pf_jurisdictions_pf_jurisdictions" ON "PfFramework_pf_jurisdictions" (pf_jurisdictions);

CREATE TABLE "PfFramework_pf_ict_systems" (
	"PfFramework_pf_id" TEXT,
	pf_ict_systems TEXT,
	PRIMARY KEY ("PfFramework_pf_id", pf_ict_systems),
	FOREIGN KEY("PfFramework_pf_id") REFERENCES "PfFramework" (pf_id)
);
CREATE INDEX "ix_PfFramework_pf_ict_systems_pf_ict_systems" ON "PfFramework_pf_ict_systems" (pf_ict_systems);
CREATE INDEX "ix_PfFramework_pf_ict_systems_PfFramework_pf_id" ON "PfFramework_pf_ict_systems" ("PfFramework_pf_id");

CREATE TABLE "PfPiiPrincipal_pf_jurisdictions" (
	"PfPiiPrincipal_pf_id" TEXT,
	pf_jurisdictions TEXT,
	PRIMARY KEY ("PfPiiPrincipal_pf_id", pf_jurisdictions),
	FOREIGN KEY("PfPiiPrincipal_pf_id") REFERENCES "PfPiiPrincipal" (pf_id)
);
CREATE INDEX "ix_PfPiiPrincipal_pf_jurisdictions_pf_jurisdictions" ON "PfPiiPrincipal_pf_jurisdictions" (pf_jurisdictions);
CREATE INDEX "ix_PfPiiPrincipal_pf_jurisdictions_PfPiiPrincipal_pf_id" ON "PfPiiPrincipal_pf_jurisdictions" ("PfPiiPrincipal_pf_id");

CREATE TABLE "PfPiiProcessor_pf_sub_processors" (
	"PfPiiProcessor_pf_id" TEXT,
	pf_sub_processors_pf_id TEXT,
	PRIMARY KEY ("PfPiiProcessor_pf_id", pf_sub_processors_pf_id),
	FOREIGN KEY("PfPiiProcessor_pf_id") REFERENCES "PfPiiProcessor" (pf_id),
	FOREIGN KEY(pf_sub_processors_pf_id) REFERENCES "PfPiiProcessor" (pf_id)
);
CREATE INDEX "ix_PfPiiProcessor_pf_sub_processors_PfPiiProcessor_pf_id" ON "PfPiiProcessor_pf_sub_processors" ("PfPiiProcessor_pf_id");
CREATE INDEX "ix_PfPiiProcessor_pf_sub_processors_pf_sub_processors_pf_id" ON "PfPiiProcessor_pf_sub_processors" (pf_sub_processors_pf_id);

CREATE TABLE "PfPiiProcessor_pf_jurisdictions" (
	"PfPiiProcessor_pf_id" TEXT,
	pf_jurisdictions TEXT,
	PRIMARY KEY ("PfPiiProcessor_pf_id", pf_jurisdictions),
	FOREIGN KEY("PfPiiProcessor_pf_id") REFERENCES "PfPiiProcessor" (pf_id)
);
CREATE INDEX "ix_PfPiiProcessor_pf_jurisdictions_pf_jurisdictions" ON "PfPiiProcessor_pf_jurisdictions" (pf_jurisdictions);
CREATE INDEX "ix_PfPiiProcessor_pf_jurisdictions_PfPiiProcessor_pf_id" ON "PfPiiProcessor_pf_jurisdictions" ("PfPiiProcessor_pf_id");

CREATE TABLE "PfThirdParty_pf_jurisdictions" (
	"PfThirdParty_pf_id" TEXT,
	pf_jurisdictions TEXT,
	PRIMARY KEY ("PfThirdParty_pf_id", pf_jurisdictions),
	FOREIGN KEY("PfThirdParty_pf_id") REFERENCES "PfThirdParty" (pf_id)
);
CREATE INDEX "ix_PfThirdParty_pf_jurisdictions_PfThirdParty_pf_id" ON "PfThirdParty_pf_jurisdictions" ("PfThirdParty_pf_id");
CREATE INDEX "ix_PfThirdParty_pf_jurisdictions_pf_jurisdictions" ON "PfThirdParty_pf_jurisdictions" (pf_jurisdictions);

CREATE TABLE "PfPiiController" (
	pf_controller_policy TEXT,
	pf_privacy_officer TEXT,
	pf_actor_type TEXT NOT NULL,
	pf_contact TEXT,
	pf_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (pf_id),
	FOREIGN KEY(pf_controller_policy) REFERENCES "PfPolicy" (pf_id)
);
CREATE INDEX "ix_PfPiiController_pf_id" ON "PfPiiController" (pf_id);

CREATE TABLE "PfPiiFlow" (
	pf_provider TEXT NOT NULL,
	pf_recipient TEXT NOT NULL,
	pf_decides_afterwards TEXT,
	pf_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	"PfFramework_pf_id" TEXT,
	PRIMARY KEY (pf_id),
	FOREIGN KEY(pf_provider) REFERENCES "PfActor" (pf_id),
	FOREIGN KEY(pf_recipient) REFERENCES "PfActor" (pf_id),
	FOREIGN KEY(pf_decides_afterwards) REFERENCES "PfActor" (pf_id),
	FOREIGN KEY("PfFramework_pf_id") REFERENCES "PfFramework" (pf_id)
);
CREATE INDEX "ix_PfPiiFlow_pf_id" ON "PfPiiFlow" (pf_id);

CREATE TABLE "PfControl" (
	pf_control_kind VARCHAR(28) NOT NULL,
	pf_control_objective TEXT,
	pf_control_detail TEXT,
	pf_control_responsible TEXT,
	pf_control_state VARCHAR(12),
	pf_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	"PfFramework_pf_id" TEXT,
	PRIMARY KEY (pf_id),
	FOREIGN KEY(pf_control_responsible) REFERENCES "PfActor" (pf_id),
	FOREIGN KEY("PfFramework_pf_id") REFERENCES "PfFramework" (pf_id)
);
CREATE INDEX "ix_PfControl_pf_id" ON "PfControl" (pf_id);

CREATE TABLE "PfActor_pf_jurisdictions" (
	"PfActor_pf_id" TEXT,
	pf_jurisdictions TEXT,
	PRIMARY KEY ("PfActor_pf_id", pf_jurisdictions),
	FOREIGN KEY("PfActor_pf_id") REFERENCES "PfActor" (pf_id)
);
CREATE INDEX "ix_PfActor_pf_jurisdictions_PfActor_pf_id" ON "PfActor_pf_jurisdictions" ("PfActor_pf_id");
CREATE INDEX "ix_PfActor_pf_jurisdictions_pf_jurisdictions" ON "PfActor_pf_jurisdictions" (pf_jurisdictions);

CREATE TABLE "PfPiiItem_pf_concerned_principals" (
	"PfPiiItem_pf_id" TEXT,
	pf_concerned_principals_pf_id TEXT,
	PRIMARY KEY ("PfPiiItem_pf_id", pf_concerned_principals_pf_id),
	FOREIGN KEY("PfPiiItem_pf_id") REFERENCES "PfPiiItem" (pf_id),
	FOREIGN KEY(pf_concerned_principals_pf_id) REFERENCES "PfPiiPrincipal" (pf_id)
);
CREATE INDEX "ix_PfPiiItem_pf_concerned_principals_pf_concerned_principals_pf_id" ON "PfPiiItem_pf_concerned_principals" (pf_concerned_principals_pf_id);
CREATE INDEX "ix_PfPiiItem_pf_concerned_principals_PfPiiItem_pf_id" ON "PfPiiItem_pf_concerned_principals" ("PfPiiItem_pf_id");

CREATE TABLE "PfPiiItem_pf_operations" (
	"PfPiiItem_pf_id" TEXT,
	pf_operations VARCHAR(12),
	PRIMARY KEY ("PfPiiItem_pf_id", pf_operations),
	FOREIGN KEY("PfPiiItem_pf_id") REFERENCES "PfPiiItem" (pf_id)
);
CREATE INDEX "ix_PfPiiItem_pf_operations_PfPiiItem_pf_id" ON "PfPiiItem_pf_operations" ("PfPiiItem_pf_id");
CREATE INDEX "ix_PfPiiItem_pf_operations_pf_operations" ON "PfPiiItem_pf_operations" (pf_operations);

CREATE TABLE "PfPiiItem_pf_pii_categories" (
	"PfPiiItem_pf_id" TEXT,
	pf_pii_categories TEXT,
	PRIMARY KEY ("PfPiiItem_pf_id", pf_pii_categories),
	FOREIGN KEY("PfPiiItem_pf_id") REFERENCES "PfPiiItem" (pf_id)
);
CREATE INDEX "ix_PfPiiItem_pf_pii_categories_pf_pii_categories" ON "PfPiiItem_pf_pii_categories" (pf_pii_categories);
CREATE INDEX "ix_PfPiiItem_pf_pii_categories_PfPiiItem_pf_id" ON "PfPiiItem_pf_pii_categories" ("PfPiiItem_pf_id");

CREATE TABLE "PfPiiItem_pf_recognized_by" (
	"PfPiiItem_pf_id" TEXT,
	pf_recognized_by VARCHAR(20),
	PRIMARY KEY ("PfPiiItem_pf_id", pf_recognized_by),
	FOREIGN KEY("PfPiiItem_pf_id") REFERENCES "PfPiiItem" (pf_id)
);
CREATE INDEX "ix_PfPiiItem_pf_recognized_by_pf_recognized_by" ON "PfPiiItem_pf_recognized_by" (pf_recognized_by);
CREATE INDEX "ix_PfPiiItem_pf_recognized_by_PfPiiItem_pf_id" ON "PfPiiItem_pf_recognized_by" ("PfPiiItem_pf_id");

CREATE TABLE "PfSafeguardingRequirement_pf_applies_to" (
	"PfSafeguardingRequirement_pf_id" TEXT,
	pf_applies_to_pf_id TEXT,
	PRIMARY KEY ("PfSafeguardingRequirement_pf_id", pf_applies_to_pf_id),
	FOREIGN KEY("PfSafeguardingRequirement_pf_id") REFERENCES "PfSafeguardingRequirement" (pf_id),
	FOREIGN KEY(pf_applies_to_pf_id) REFERENCES "PfActor" (pf_id)
);
CREATE INDEX "ix_PfSafeguardingRequirement_pf_applies_to_PfSafeguardingRequirement_pf_id" ON "PfSafeguardingRequirement_pf_applies_to" ("PfSafeguardingRequirement_pf_id");
CREATE INDEX "ix_PfSafeguardingRequirement_pf_applies_to_pf_applies_to_pf_id" ON "PfSafeguardingRequirement_pf_applies_to" (pf_applies_to_pf_id);

CREATE TABLE "PfPolicy_pf_purposes" (
	"PfPolicy_pf_id" TEXT,
	pf_purposes TEXT,
	PRIMARY KEY ("PfPolicy_pf_id", pf_purposes),
	FOREIGN KEY("PfPolicy_pf_id") REFERENCES "PfPolicy" (pf_id)
);
CREATE INDEX "ix_PfPolicy_pf_purposes_PfPolicy_pf_id" ON "PfPolicy_pf_purposes" ("PfPolicy_pf_id");
CREATE INDEX "ix_PfPolicy_pf_purposes_pf_purposes" ON "PfPolicy_pf_purposes" (pf_purposes);

CREATE TABLE "PfPolicy_pf_concerned_pii" (
	"PfPolicy_pf_id" TEXT,
	pf_concerned_pii_pf_id TEXT,
	PRIMARY KEY ("PfPolicy_pf_id", pf_concerned_pii_pf_id),
	FOREIGN KEY("PfPolicy_pf_id") REFERENCES "PfPolicy" (pf_id),
	FOREIGN KEY(pf_concerned_pii_pf_id) REFERENCES "PfPiiItem" (pf_id)
);
CREATE INDEX "ix_PfPolicy_pf_concerned_pii_pf_concerned_pii_pf_id" ON "PfPolicy_pf_concerned_pii" (pf_concerned_pii_pf_id);
CREATE INDEX "ix_PfPolicy_pf_concerned_pii_PfPolicy_pf_id" ON "PfPolicy_pf_concerned_pii" ("PfPolicy_pf_id");

CREATE TABLE "PfPolicy_pf_principles" (
	"PfPolicy_pf_id" TEXT,
	pf_principles VARCHAR(14),
	PRIMARY KEY ("PfPolicy_pf_id", pf_principles),
	FOREIGN KEY("PfPolicy_pf_id") REFERENCES "PfPolicy" (pf_id)
);
CREATE INDEX "ix_PfPolicy_pf_principles_pf_principles" ON "PfPolicy_pf_principles" (pf_principles);
CREATE INDEX "ix_PfPolicy_pf_principles_PfPolicy_pf_id" ON "PfPolicy_pf_principles" ("PfPolicy_pf_id");

CREATE TABLE "PfPolicy_pf_stated_rights" (
	"PfPolicy_pf_id" TEXT,
	pf_stated_rights TEXT,
	PRIMARY KEY ("PfPolicy_pf_id", pf_stated_rights),
	FOREIGN KEY("PfPolicy_pf_id") REFERENCES "PfPolicy" (pf_id)
);
CREATE INDEX "ix_PfPolicy_pf_stated_rights_pf_stated_rights" ON "PfPolicy_pf_stated_rights" (pf_stated_rights);
CREATE INDEX "ix_PfPolicy_pf_stated_rights_PfPolicy_pf_id" ON "PfPolicy_pf_stated_rights" ("PfPolicy_pf_id");

CREATE TABLE "PfPrincipleImplementation_pf_evidence" (
	"PfPrincipleImplementation_pf_id" TEXT,
	pf_evidence TEXT,
	PRIMARY KEY ("PfPrincipleImplementation_pf_id", pf_evidence),
	FOREIGN KEY("PfPrincipleImplementation_pf_id") REFERENCES "PfPrincipleImplementation" (pf_id)
);
CREATE INDEX "ix_PfPrincipleImplementation_pf_evidence_PfPrincipleImplementation_pf_id" ON "PfPrincipleImplementation_pf_evidence" ("PfPrincipleImplementation_pf_id");
CREATE INDEX "ix_PfPrincipleImplementation_pf_evidence_pf_evidence" ON "PfPrincipleImplementation_pf_evidence" (pf_evidence);

CREATE TABLE "PfPrincipleImplementation_pf_measures" (
	"PfPrincipleImplementation_pf_id" TEXT,
	pf_measures TEXT,
	PRIMARY KEY ("PfPrincipleImplementation_pf_id", pf_measures),
	FOREIGN KEY("PfPrincipleImplementation_pf_id") REFERENCES "PfPrincipleImplementation" (pf_id)
);
CREATE INDEX "ix_PfPrincipleImplementation_pf_measures_PfPrincipleImplementation_pf_id" ON "PfPrincipleImplementation_pf_measures" ("PfPrincipleImplementation_pf_id");
CREATE INDEX "ix_PfPrincipleImplementation_pf_measures_pf_measures" ON "PfPrincipleImplementation_pf_measures" (pf_measures);

CREATE TABLE "PfPrincipleImplementation_pf_gaps" (
	"PfPrincipleImplementation_pf_id" TEXT,
	pf_gaps TEXT,
	PRIMARY KEY ("PfPrincipleImplementation_pf_id", pf_gaps),
	FOREIGN KEY("PfPrincipleImplementation_pf_id") REFERENCES "PfPrincipleImplementation" (pf_id)
);
CREATE INDEX "ix_PfPrincipleImplementation_pf_gaps_pf_gaps" ON "PfPrincipleImplementation_pf_gaps" (pf_gaps);
CREATE INDEX "ix_PfPrincipleImplementation_pf_gaps_PfPrincipleImplementation_pf_id" ON "PfPrincipleImplementation_pf_gaps" ("PfPrincipleImplementation_pf_id");

CREATE TABLE "PfPrincipleImplementation_pf_improvements" (
	"PfPrincipleImplementation_pf_id" TEXT,
	pf_improvements TEXT,
	PRIMARY KEY ("PfPrincipleImplementation_pf_id", pf_improvements),
	FOREIGN KEY("PfPrincipleImplementation_pf_id") REFERENCES "PfPrincipleImplementation" (pf_id)
);
CREATE INDEX "ix_PfPrincipleImplementation_pf_improvements_PfPrincipleImplementation_pf_id" ON "PfPrincipleImplementation_pf_improvements" ("PfPrincipleImplementation_pf_id");
CREATE INDEX "ix_PfPrincipleImplementation_pf_improvements_pf_improvements" ON "PfPrincipleImplementation_pf_improvements" (pf_improvements);

CREATE TABLE "PfRisk_pf_concerned_pii" (
	"PfRisk_pf_id" TEXT,
	pf_concerned_pii_pf_id TEXT,
	PRIMARY KEY ("PfRisk_pf_id", pf_concerned_pii_pf_id),
	FOREIGN KEY("PfRisk_pf_id") REFERENCES "PfRisk" (pf_id),
	FOREIGN KEY(pf_concerned_pii_pf_id) REFERENCES "PfPiiItem" (pf_id)
);
CREATE INDEX "ix_PfRisk_pf_concerned_pii_pf_concerned_pii_pf_id" ON "PfRisk_pf_concerned_pii" (pf_concerned_pii_pf_id);
CREATE INDEX "ix_PfRisk_pf_concerned_pii_PfRisk_pf_id" ON "PfRisk_pf_concerned_pii" ("PfRisk_pf_id");

CREATE TABLE "PfRisk_pf_concerned_principals" (
	"PfRisk_pf_id" TEXT,
	pf_concerned_principals_pf_id TEXT,
	PRIMARY KEY ("PfRisk_pf_id", pf_concerned_principals_pf_id),
	FOREIGN KEY("PfRisk_pf_id") REFERENCES "PfRisk" (pf_id),
	FOREIGN KEY(pf_concerned_principals_pf_id) REFERENCES "PfPiiPrincipal" (pf_id)
);
CREATE INDEX "ix_PfRisk_pf_concerned_principals_pf_concerned_principals_pf_id" ON "PfRisk_pf_concerned_principals" (pf_concerned_principals_pf_id);
CREATE INDEX "ix_PfRisk_pf_concerned_principals_PfRisk_pf_id" ON "PfRisk_pf_concerned_principals" ("PfRisk_pf_id");

CREATE TABLE "PfImpactAssessment_pf_risks_found" (
	"PfImpactAssessment_pf_id" TEXT,
	pf_risks_found_pf_id TEXT,
	PRIMARY KEY ("PfImpactAssessment_pf_id", pf_risks_found_pf_id),
	FOREIGN KEY("PfImpactAssessment_pf_id") REFERENCES "PfImpactAssessment" (pf_id),
	FOREIGN KEY(pf_risks_found_pf_id) REFERENCES "PfRisk" (pf_id)
);
CREATE INDEX "ix_PfImpactAssessment_pf_risks_found_pf_risks_found_pf_id" ON "PfImpactAssessment_pf_risks_found" (pf_risks_found_pf_id);
CREATE INDEX "ix_PfImpactAssessment_pf_risks_found_PfImpactAssessment_pf_id" ON "PfImpactAssessment_pf_risks_found" ("PfImpactAssessment_pf_id");

CREATE TABLE "PfImpactAssessment_pf_risks_treated" (
	"PfImpactAssessment_pf_id" TEXT,
	pf_risks_treated_pf_id TEXT,
	PRIMARY KEY ("PfImpactAssessment_pf_id", pf_risks_treated_pf_id),
	FOREIGN KEY("PfImpactAssessment_pf_id") REFERENCES "PfImpactAssessment" (pf_id),
	FOREIGN KEY(pf_risks_treated_pf_id) REFERENCES "PfRisk" (pf_id)
);
CREATE INDEX "ix_PfImpactAssessment_pf_risks_treated_PfImpactAssessment_pf_id" ON "PfImpactAssessment_pf_risks_treated" ("PfImpactAssessment_pf_id");
CREATE INDEX "ix_PfImpactAssessment_pf_risks_treated_pf_risks_treated_pf_id" ON "PfImpactAssessment_pf_risks_treated" (pf_risks_treated_pf_id);

CREATE TABLE "PfImpactAssessment_pf_risks_accepted" (
	"PfImpactAssessment_pf_id" TEXT,
	pf_risks_accepted_pf_id TEXT,
	PRIMARY KEY ("PfImpactAssessment_pf_id", pf_risks_accepted_pf_id),
	FOREIGN KEY("PfImpactAssessment_pf_id") REFERENCES "PfImpactAssessment" (pf_id),
	FOREIGN KEY(pf_risks_accepted_pf_id) REFERENCES "PfRisk" (pf_id)
);
CREATE INDEX "ix_PfImpactAssessment_pf_risks_accepted_PfImpactAssessment_pf_id" ON "PfImpactAssessment_pf_risks_accepted" ("PfImpactAssessment_pf_id");
CREATE INDEX "ix_PfImpactAssessment_pf_risks_accepted_pf_risks_accepted_pf_id" ON "PfImpactAssessment_pf_risks_accepted" (pf_risks_accepted_pf_id);

CREATE TABLE "PfImpactAssessment_pf_consultations" (
	"PfImpactAssessment_pf_id" TEXT,
	pf_consultations TEXT,
	PRIMARY KEY ("PfImpactAssessment_pf_id", pf_consultations),
	FOREIGN KEY("PfImpactAssessment_pf_id") REFERENCES "PfImpactAssessment" (pf_id)
);
CREATE INDEX "ix_PfImpactAssessment_pf_consultations_pf_consultations" ON "PfImpactAssessment_pf_consultations" (pf_consultations);
CREATE INDEX "ix_PfImpactAssessment_pf_consultations_PfImpactAssessment_pf_id" ON "PfImpactAssessment_pf_consultations" ("PfImpactAssessment_pf_id");

CREATE TABLE "PfBreach_pf_concerned_pii" (
	"PfBreach_pf_id" TEXT,
	pf_concerned_pii_pf_id TEXT,
	PRIMARY KEY ("PfBreach_pf_id", pf_concerned_pii_pf_id),
	FOREIGN KEY("PfBreach_pf_id") REFERENCES "PfBreach" (pf_id),
	FOREIGN KEY(pf_concerned_pii_pf_id) REFERENCES "PfPiiItem" (pf_id)
);
CREATE INDEX "ix_PfBreach_pf_concerned_pii_PfBreach_pf_id" ON "PfBreach_pf_concerned_pii" ("PfBreach_pf_id");
CREATE INDEX "ix_PfBreach_pf_concerned_pii_pf_concerned_pii_pf_id" ON "PfBreach_pf_concerned_pii" (pf_concerned_pii_pf_id);

CREATE TABLE "PfBreach_pf_breached_requirements" (
	"PfBreach_pf_id" TEXT,
	pf_breached_requirements_pf_id TEXT,
	PRIMARY KEY ("PfBreach_pf_id", pf_breached_requirements_pf_id),
	FOREIGN KEY("PfBreach_pf_id") REFERENCES "PfBreach" (pf_id),
	FOREIGN KEY(pf_breached_requirements_pf_id) REFERENCES "PfSafeguardingRequirement" (pf_id)
);
CREATE INDEX "ix_PfBreach_pf_breached_requirements_PfBreach_pf_id" ON "PfBreach_pf_breached_requirements" ("PfBreach_pf_id");
CREATE INDEX "ix_PfBreach_pf_breached_requirements_pf_breached_requirements_pf_id" ON "PfBreach_pf_breached_requirements" (pf_breached_requirements_pf_id);

CREATE TABLE "PfBreach_pf_immediate_actions" (
	"PfBreach_pf_id" TEXT,
	pf_immediate_actions TEXT,
	PRIMARY KEY ("PfBreach_pf_id", pf_immediate_actions),
	FOREIGN KEY("PfBreach_pf_id") REFERENCES "PfBreach" (pf_id)
);
CREATE INDEX "ix_PfBreach_pf_immediate_actions_PfBreach_pf_id" ON "PfBreach_pf_immediate_actions" ("PfBreach_pf_id");
CREATE INDEX "ix_PfBreach_pf_immediate_actions_pf_immediate_actions" ON "PfBreach_pf_immediate_actions" (pf_immediate_actions);

CREATE TABLE "PfBreach_pf_notifications" (
	"PfBreach_pf_id" TEXT,
	pf_notifications TEXT,
	PRIMARY KEY ("PfBreach_pf_id", pf_notifications),
	FOREIGN KEY("PfBreach_pf_id") REFERENCES "PfBreach" (pf_id)
);
CREATE INDEX "ix_PfBreach_pf_notifications_pf_notifications" ON "PfBreach_pf_notifications" (pf_notifications);
CREATE INDEX "ix_PfBreach_pf_notifications_PfBreach_pf_id" ON "PfBreach_pf_notifications" ("PfBreach_pf_id");

CREATE TABLE "PfBreach_pf_remediation" (
	"PfBreach_pf_id" TEXT,
	pf_remediation TEXT,
	PRIMARY KEY ("PfBreach_pf_id", pf_remediation),
	FOREIGN KEY("PfBreach_pf_id") REFERENCES "PfBreach" (pf_id)
);
CREATE INDEX "ix_PfBreach_pf_remediation_PfBreach_pf_id" ON "PfBreach_pf_remediation" ("PfBreach_pf_id");
CREATE INDEX "ix_PfBreach_pf_remediation_pf_remediation" ON "PfBreach_pf_remediation" (pf_remediation);

CREATE TABLE "PfConsent_pf_purposes" (
	"PfConsent_pf_id" TEXT,
	pf_purposes TEXT,
	PRIMARY KEY ("PfConsent_pf_id", pf_purposes),
	FOREIGN KEY("PfConsent_pf_id") REFERENCES "PfConsent" (pf_id)
);
CREATE INDEX "ix_PfConsent_pf_purposes_pf_purposes" ON "PfConsent_pf_purposes" (pf_purposes);
CREATE INDEX "ix_PfConsent_pf_purposes_PfConsent_pf_id" ON "PfConsent_pf_purposes" ("PfConsent_pf_id");

CREATE TABLE "PfConsent_pf_concerned_pii" (
	"PfConsent_pf_id" TEXT,
	pf_concerned_pii_pf_id TEXT,
	PRIMARY KEY ("PfConsent_pf_id", pf_concerned_pii_pf_id),
	FOREIGN KEY("PfConsent_pf_id") REFERENCES "PfConsent" (pf_id),
	FOREIGN KEY(pf_concerned_pii_pf_id) REFERENCES "PfPiiItem" (pf_id)
);
CREATE INDEX "ix_PfConsent_pf_concerned_pii_pf_concerned_pii_pf_id" ON "PfConsent_pf_concerned_pii" (pf_concerned_pii_pf_id);
CREATE INDEX "ix_PfConsent_pf_concerned_pii_PfConsent_pf_id" ON "PfConsent_pf_concerned_pii" ("PfConsent_pf_id");

CREATE TABLE "PfConsent_pf_evidence" (
	"PfConsent_pf_id" TEXT,
	pf_evidence TEXT,
	PRIMARY KEY ("PfConsent_pf_id", pf_evidence),
	FOREIGN KEY("PfConsent_pf_id") REFERENCES "PfConsent" (pf_id)
);
CREATE INDEX "ix_PfConsent_pf_evidence_pf_evidence" ON "PfConsent_pf_evidence" (pf_evidence);
CREATE INDEX "ix_PfConsent_pf_evidence_PfConsent_pf_id" ON "PfConsent_pf_evidence" ("PfConsent_pf_id");

CREATE TABLE "PfPreference_pf_refused_operations" (
	"PfPreference_pf_id" TEXT,
	pf_refused_operations VARCHAR(12),
	PRIMARY KEY ("PfPreference_pf_id", pf_refused_operations),
	FOREIGN KEY("PfPreference_pf_id") REFERENCES "PfPreference" (pf_id)
);
CREATE INDEX "ix_PfPreference_pf_refused_operations_PfPreference_pf_id" ON "PfPreference_pf_refused_operations" ("PfPreference_pf_id");
CREATE INDEX "ix_PfPreference_pf_refused_operations_pf_refused_operations" ON "PfPreference_pf_refused_operations" (pf_refused_operations);

CREATE TABLE "PfPreference_pf_refused_recipients" (
	"PfPreference_pf_id" TEXT,
	pf_refused_recipients TEXT,
	PRIMARY KEY ("PfPreference_pf_id", pf_refused_recipients),
	FOREIGN KEY("PfPreference_pf_id") REFERENCES "PfPreference" (pf_id)
);
CREATE INDEX "ix_PfPreference_pf_refused_recipients_PfPreference_pf_id" ON "PfPreference_pf_refused_recipients" ("PfPreference_pf_id");
CREATE INDEX "ix_PfPreference_pf_refused_recipients_pf_refused_recipients" ON "PfPreference_pf_refused_recipients" (pf_refused_recipients);

CREATE TABLE "PfProcessingActivity" (
	pf_retention TEXT,
	pf_controller TEXT NOT NULL,
	pf_crosses_borders BOOLEAN,
	pf_id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	"PfFramework_pf_id" TEXT,
	PRIMARY KEY (pf_id),
	FOREIGN KEY(pf_controller) REFERENCES "PfPiiController" (pf_id),
	FOREIGN KEY("PfFramework_pf_id") REFERENCES "PfFramework" (pf_id)
);
CREATE INDEX "ix_PfProcessingActivity_pf_id" ON "PfProcessingActivity" (pf_id);

CREATE TABLE "PfPiiController_pf_purposes" (
	"PfPiiController_pf_id" TEXT,
	pf_purposes TEXT,
	PRIMARY KEY ("PfPiiController_pf_id", pf_purposes),
	FOREIGN KEY("PfPiiController_pf_id") REFERENCES "PfPiiController" (pf_id)
);
CREATE INDEX "ix_PfPiiController_pf_purposes_PfPiiController_pf_id" ON "PfPiiController_pf_purposes" ("PfPiiController_pf_id");
CREATE INDEX "ix_PfPiiController_pf_purposes_pf_purposes" ON "PfPiiController_pf_purposes" (pf_purposes);

CREATE TABLE "PfPiiController_pf_legal_bases" (
	"PfPiiController_pf_id" TEXT,
	pf_legal_bases TEXT,
	PRIMARY KEY ("PfPiiController_pf_id", pf_legal_bases),
	FOREIGN KEY("PfPiiController_pf_id") REFERENCES "PfPiiController" (pf_id)
);
CREATE INDEX "ix_PfPiiController_pf_legal_bases_PfPiiController_pf_id" ON "PfPiiController_pf_legal_bases" ("PfPiiController_pf_id");
CREATE INDEX "ix_PfPiiController_pf_legal_bases_pf_legal_bases" ON "PfPiiController_pf_legal_bases" (pf_legal_bases);

CREATE TABLE "PfPiiController_pf_appointed_processors" (
	"PfPiiController_pf_id" TEXT,
	pf_appointed_processors_pf_id TEXT,
	PRIMARY KEY ("PfPiiController_pf_id", pf_appointed_processors_pf_id),
	FOREIGN KEY("PfPiiController_pf_id") REFERENCES "PfPiiController" (pf_id),
	FOREIGN KEY(pf_appointed_processors_pf_id) REFERENCES "PfPiiProcessor" (pf_id)
);
CREATE INDEX "ix_PfPiiController_pf_appointed_processors_PfPiiController_pf_id" ON "PfPiiController_pf_appointed_processors" ("PfPiiController_pf_id");
CREATE INDEX "ix_PfPiiController_pf_appointed_processors_pf_appointed_processors_pf_id" ON "PfPiiController_pf_appointed_processors" (pf_appointed_processors_pf_id);

CREATE TABLE "PfPiiController_pf_jurisdictions" (
	"PfPiiController_pf_id" TEXT,
	pf_jurisdictions TEXT,
	PRIMARY KEY ("PfPiiController_pf_id", pf_jurisdictions),
	FOREIGN KEY("PfPiiController_pf_id") REFERENCES "PfPiiController" (pf_id)
);
CREATE INDEX "ix_PfPiiController_pf_jurisdictions_pf_jurisdictions" ON "PfPiiController_pf_jurisdictions" (pf_jurisdictions);
CREATE INDEX "ix_PfPiiController_pf_jurisdictions_PfPiiController_pf_id" ON "PfPiiController_pf_jurisdictions" ("PfPiiController_pf_id");

CREATE TABLE "PfPiiProcessor_pf_instructing_controllers" (
	"PfPiiProcessor_pf_id" TEXT,
	pf_instructing_controllers_pf_id TEXT,
	PRIMARY KEY ("PfPiiProcessor_pf_id", pf_instructing_controllers_pf_id),
	FOREIGN KEY("PfPiiProcessor_pf_id") REFERENCES "PfPiiProcessor" (pf_id),
	FOREIGN KEY(pf_instructing_controllers_pf_id) REFERENCES "PfPiiController" (pf_id)
);
CREATE INDEX "ix_PfPiiProcessor_pf_instructing_controllers_PfPiiProcessor_pf_id" ON "PfPiiProcessor_pf_instructing_controllers" ("PfPiiProcessor_pf_id");
CREATE INDEX "ix_PfPiiProcessor_pf_instructing_controllers_pf_instructing_controllers_pf_id" ON "PfPiiProcessor_pf_instructing_controllers" (pf_instructing_controllers_pf_id);

CREATE TABLE "PfPiiFlow_pf_concerned_pii" (
	"PfPiiFlow_pf_id" TEXT,
	pf_concerned_pii_pf_id TEXT,
	PRIMARY KEY ("PfPiiFlow_pf_id", pf_concerned_pii_pf_id),
	FOREIGN KEY("PfPiiFlow_pf_id") REFERENCES "PfPiiFlow" (pf_id),
	FOREIGN KEY(pf_concerned_pii_pf_id) REFERENCES "PfPiiItem" (pf_id)
);
CREATE INDEX "ix_PfPiiFlow_pf_concerned_pii_pf_concerned_pii_pf_id" ON "PfPiiFlow_pf_concerned_pii" (pf_concerned_pii_pf_id);
CREATE INDEX "ix_PfPiiFlow_pf_concerned_pii_PfPiiFlow_pf_id" ON "PfPiiFlow_pf_concerned_pii" ("PfPiiFlow_pf_id");

CREATE TABLE "PfSafeguardingRequirement_pf_met_by" (
	"PfSafeguardingRequirement_pf_id" TEXT,
	pf_met_by_pf_id TEXT,
	PRIMARY KEY ("PfSafeguardingRequirement_pf_id", pf_met_by_pf_id),
	FOREIGN KEY("PfSafeguardingRequirement_pf_id") REFERENCES "PfSafeguardingRequirement" (pf_id),
	FOREIGN KEY(pf_met_by_pf_id) REFERENCES "PfControl" (pf_id)
);
CREATE INDEX "ix_PfSafeguardingRequirement_pf_met_by_pf_met_by_pf_id" ON "PfSafeguardingRequirement_pf_met_by" (pf_met_by_pf_id);
CREATE INDEX "ix_PfSafeguardingRequirement_pf_met_by_PfSafeguardingRequirement_pf_id" ON "PfSafeguardingRequirement_pf_met_by" ("PfSafeguardingRequirement_pf_id");

CREATE TABLE "PfControl_pf_principles" (
	"PfControl_pf_id" TEXT,
	pf_principles VARCHAR(14),
	PRIMARY KEY ("PfControl_pf_id", pf_principles),
	FOREIGN KEY("PfControl_pf_id") REFERENCES "PfControl" (pf_id)
);
CREATE INDEX "ix_PfControl_pf_principles_pf_principles" ON "PfControl_pf_principles" (pf_principles);
CREATE INDEX "ix_PfControl_pf_principles_PfControl_pf_id" ON "PfControl_pf_principles" ("PfControl_pf_id");

CREATE TABLE "PfControl_pf_evidence" (
	"PfControl_pf_id" TEXT,
	pf_evidence TEXT,
	PRIMARY KEY ("PfControl_pf_id", pf_evidence),
	FOREIGN KEY("PfControl_pf_id") REFERENCES "PfControl" (pf_id)
);
CREATE INDEX "ix_PfControl_pf_evidence_pf_evidence" ON "PfControl_pf_evidence" (pf_evidence);
CREATE INDEX "ix_PfControl_pf_evidence_PfControl_pf_id" ON "PfControl_pf_evidence" ("PfControl_pf_id");

CREATE TABLE "PfControl_pf_answers_requirements" (
	"PfControl_pf_id" TEXT,
	pf_answers_requirements_pf_id TEXT,
	PRIMARY KEY ("PfControl_pf_id", pf_answers_requirements_pf_id),
	FOREIGN KEY("PfControl_pf_id") REFERENCES "PfControl" (pf_id),
	FOREIGN KEY(pf_answers_requirements_pf_id) REFERENCES "PfSafeguardingRequirement" (pf_id)
);
CREATE INDEX "ix_PfControl_pf_answers_requirements_pf_answers_requirements_pf_id" ON "PfControl_pf_answers_requirements" (pf_answers_requirements_pf_id);
CREATE INDEX "ix_PfControl_pf_answers_requirements_PfControl_pf_id" ON "PfControl_pf_answers_requirements" ("PfControl_pf_id");

CREATE TABLE "PfPrincipleImplementation_pf_related_controls" (
	"PfPrincipleImplementation_pf_id" TEXT,
	pf_related_controls_pf_id TEXT,
	PRIMARY KEY ("PfPrincipleImplementation_pf_id", pf_related_controls_pf_id),
	FOREIGN KEY("PfPrincipleImplementation_pf_id") REFERENCES "PfPrincipleImplementation" (pf_id),
	FOREIGN KEY(pf_related_controls_pf_id) REFERENCES "PfControl" (pf_id)
);
CREATE INDEX "ix_PfPrincipleImplementation_pf_related_controls_PfPrincipleImplementation_pf_id" ON "PfPrincipleImplementation_pf_related_controls" ("PfPrincipleImplementation_pf_id");
CREATE INDEX "ix_PfPrincipleImplementation_pf_related_controls_pf_related_controls_pf_id" ON "PfPrincipleImplementation_pf_related_controls" (pf_related_controls_pf_id);

CREATE TABLE "PfRisk_pf_related_controls" (
	"PfRisk_pf_id" TEXT,
	pf_related_controls_pf_id TEXT,
	PRIMARY KEY ("PfRisk_pf_id", pf_related_controls_pf_id),
	FOREIGN KEY("PfRisk_pf_id") REFERENCES "PfRisk" (pf_id),
	FOREIGN KEY(pf_related_controls_pf_id) REFERENCES "PfControl" (pf_id)
);
CREATE INDEX "ix_PfRisk_pf_related_controls_pf_related_controls_pf_id" ON "PfRisk_pf_related_controls" (pf_related_controls_pf_id);
CREATE INDEX "ix_PfRisk_pf_related_controls_PfRisk_pf_id" ON "PfRisk_pf_related_controls" ("PfRisk_pf_id");

CREATE TABLE "PfProcessingActivity_pf_purposes" (
	"PfProcessingActivity_pf_id" TEXT,
	pf_purposes TEXT,
	PRIMARY KEY ("PfProcessingActivity_pf_id", pf_purposes),
	FOREIGN KEY("PfProcessingActivity_pf_id") REFERENCES "PfProcessingActivity" (pf_id)
);
CREATE INDEX "ix_PfProcessingActivity_pf_purposes_PfProcessingActivity_pf_id" ON "PfProcessingActivity_pf_purposes" ("PfProcessingActivity_pf_id");
CREATE INDEX "ix_PfProcessingActivity_pf_purposes_pf_purposes" ON "PfProcessingActivity_pf_purposes" (pf_purposes);

CREATE TABLE "PfProcessingActivity_pf_legal_bases" (
	"PfProcessingActivity_pf_id" TEXT,
	pf_legal_bases TEXT,
	PRIMARY KEY ("PfProcessingActivity_pf_id", pf_legal_bases),
	FOREIGN KEY("PfProcessingActivity_pf_id") REFERENCES "PfProcessingActivity" (pf_id)
);
CREATE INDEX "ix_PfProcessingActivity_pf_legal_bases_PfProcessingActivity_pf_id" ON "PfProcessingActivity_pf_legal_bases" ("PfProcessingActivity_pf_id");
CREATE INDEX "ix_PfProcessingActivity_pf_legal_bases_pf_legal_bases" ON "PfProcessingActivity_pf_legal_bases" (pf_legal_bases);

CREATE TABLE "PfProcessingActivity_pf_operations" (
	"PfProcessingActivity_pf_id" TEXT,
	pf_operations VARCHAR(12),
	PRIMARY KEY ("PfProcessingActivity_pf_id", pf_operations),
	FOREIGN KEY("PfProcessingActivity_pf_id") REFERENCES "PfProcessingActivity" (pf_id)
);
CREATE INDEX "ix_PfProcessingActivity_pf_operations_pf_operations" ON "PfProcessingActivity_pf_operations" (pf_operations);
CREATE INDEX "ix_PfProcessingActivity_pf_operations_PfProcessingActivity_pf_id" ON "PfProcessingActivity_pf_operations" ("PfProcessingActivity_pf_id");

CREATE TABLE "PfProcessingActivity_pf_concerned_pii" (
	"PfProcessingActivity_pf_id" TEXT,
	pf_concerned_pii_pf_id TEXT,
	PRIMARY KEY ("PfProcessingActivity_pf_id", pf_concerned_pii_pf_id),
	FOREIGN KEY("PfProcessingActivity_pf_id") REFERENCES "PfProcessingActivity" (pf_id),
	FOREIGN KEY(pf_concerned_pii_pf_id) REFERENCES "PfPiiItem" (pf_id)
);
CREATE INDEX "ix_PfProcessingActivity_pf_concerned_pii_pf_concerned_pii_pf_id" ON "PfProcessingActivity_pf_concerned_pii" (pf_concerned_pii_pf_id);
CREATE INDEX "ix_PfProcessingActivity_pf_concerned_pii_PfProcessingActivity_pf_id" ON "PfProcessingActivity_pf_concerned_pii" ("PfProcessingActivity_pf_id");

CREATE TABLE "PfProcessingActivity_pf_related_controls" (
	"PfProcessingActivity_pf_id" TEXT,
	pf_related_controls_pf_id TEXT,
	PRIMARY KEY ("PfProcessingActivity_pf_id", pf_related_controls_pf_id),
	FOREIGN KEY("PfProcessingActivity_pf_id") REFERENCES "PfProcessingActivity" (pf_id),
	FOREIGN KEY(pf_related_controls_pf_id) REFERENCES "PfControl" (pf_id)
);
CREATE INDEX "ix_PfProcessingActivity_pf_related_controls_pf_related_controls_pf_id" ON "PfProcessingActivity_pf_related_controls" (pf_related_controls_pf_id);
CREATE INDEX "ix_PfProcessingActivity_pf_related_controls_PfProcessingActivity_pf_id" ON "PfProcessingActivity_pf_related_controls" ("PfProcessingActivity_pf_id");

CREATE TABLE "PfProcessingActivity_pf_processors" (
	"PfProcessingActivity_pf_id" TEXT,
	pf_processors_pf_id TEXT,
	PRIMARY KEY ("PfProcessingActivity_pf_id", pf_processors_pf_id),
	FOREIGN KEY("PfProcessingActivity_pf_id") REFERENCES "PfProcessingActivity" (pf_id),
	FOREIGN KEY(pf_processors_pf_id) REFERENCES "PfPiiProcessor" (pf_id)
);
CREATE INDEX "ix_PfProcessingActivity_pf_processors_PfProcessingActivity_pf_id" ON "PfProcessingActivity_pf_processors" ("PfProcessingActivity_pf_id");
CREATE INDEX "ix_PfProcessingActivity_pf_processors_pf_processors_pf_id" ON "PfProcessingActivity_pf_processors" (pf_processors_pf_id);

CREATE TABLE "PfProcessingActivity_pf_activity_flows" (
	"PfProcessingActivity_pf_id" TEXT,
	pf_activity_flows_pf_id TEXT,
	PRIMARY KEY ("PfProcessingActivity_pf_id", pf_activity_flows_pf_id),
	FOREIGN KEY("PfProcessingActivity_pf_id") REFERENCES "PfProcessingActivity" (pf_id),
	FOREIGN KEY(pf_activity_flows_pf_id) REFERENCES "PfPiiFlow" (pf_id)
);
CREATE INDEX "ix_PfProcessingActivity_pf_activity_flows_PfProcessingActivity_pf_id" ON "PfProcessingActivity_pf_activity_flows" ("PfProcessingActivity_pf_id");
CREATE INDEX "ix_PfProcessingActivity_pf_activity_flows_pf_activity_flows_pf_id" ON "PfProcessingActivity_pf_activity_flows" (pf_activity_flows_pf_id);

CREATE TABLE "PfProcessingActivity_pf_sensitivities" (
	"PfProcessingActivity_pf_id" TEXT,
	pf_sensitivities VARCHAR(9),
	PRIMARY KEY ("PfProcessingActivity_pf_id", pf_sensitivities),
	FOREIGN KEY("PfProcessingActivity_pf_id") REFERENCES "PfProcessingActivity" (pf_id)
);
CREATE INDEX "ix_PfProcessingActivity_pf_sensitivities_PfProcessingActivity_pf_id" ON "PfProcessingActivity_pf_sensitivities" ("PfProcessingActivity_pf_id");
CREATE INDEX "ix_PfProcessingActivity_pf_sensitivities_pf_sensitivities" ON "PfProcessingActivity_pf_sensitivities" (pf_sensitivities);

CREATE TABLE "PfProcessingActivity_pf_transfer_safeguards" (
	"PfProcessingActivity_pf_id" TEXT,
	pf_transfer_safeguards TEXT,
	PRIMARY KEY ("PfProcessingActivity_pf_id", pf_transfer_safeguards),
	FOREIGN KEY("PfProcessingActivity_pf_id") REFERENCES "PfProcessingActivity" (pf_id)
);
CREATE INDEX "ix_PfProcessingActivity_pf_transfer_safeguards_PfProcessingActivity_pf_id" ON "PfProcessingActivity_pf_transfer_safeguards" ("PfProcessingActivity_pf_id");
CREATE INDEX "ix_PfProcessingActivity_pf_transfer_safeguards_pf_transfer_safeguards" ON "PfProcessingActivity_pf_transfer_safeguards" (pf_transfer_safeguards);

CREATE TABLE "PfImpactAssessment_pf_assessed_activities" (
	"PfImpactAssessment_pf_id" TEXT,
	pf_assessed_activities_pf_id TEXT,
	PRIMARY KEY ("PfImpactAssessment_pf_id", pf_assessed_activities_pf_id),
	FOREIGN KEY("PfImpactAssessment_pf_id") REFERENCES "PfImpactAssessment" (pf_id),
	FOREIGN KEY(pf_assessed_activities_pf_id) REFERENCES "PfProcessingActivity" (pf_id)
);
CREATE INDEX "ix_PfImpactAssessment_pf_assessed_activities_PfImpactAssessment_pf_id" ON "PfImpactAssessment_pf_assessed_activities" ("PfImpactAssessment_pf_id");
CREATE INDEX "ix_PfImpactAssessment_pf_assessed_activities_pf_assessed_activities_pf_id" ON "PfImpactAssessment_pf_assessed_activities" (pf_assessed_activities_pf_id);
