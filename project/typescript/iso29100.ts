export type PfRecordMixinPfId = string;
export type PfFrameworkPfId = string;
export type PfActorPfId = string;
export type PfPiiPrincipalPfId = string;
export type PfPiiControllerPfId = string;
export type PfPiiProcessorPfId = string;
export type PfThirdPartyPfId = string;
export type PfPiiItemPfId = string;
export type PfPiiFlowPfId = string;
export type PfProcessingActivityPfId = string;
export type PfSafeguardingRequirementPfId = string;
export type PfPolicyPfId = string;
export type PfControlPfId = string;
export type PfPrincipleImplementationPfId = string;
export type PfRiskPfId = string;
export type PfImpactAssessmentPfId = string;
export type PfBreachPfId = string;
export type PfConsentPfId = string;
export type PfPreferencePfId = string;
/**
* The privacy principles by their subclause numbers. A value's title and description are this project's own summary, and the principles' headings and wording are ISO's.
*/
export enum PfPrinciple {
    
    /** People get a say in whether their PII is processed, can agree or refuse purpose by purpose, and can change their minds later. */
    number_6FULL_STOP2_People_decide = "principle_6_2",
    /** The law allows each reason for processing, and people are told the reason before their PII is gathered, or at that moment. */
    number_6FULL_STOP3_Lawful_stated_reasons = "principle_6_3",
    /** The organization gathers only the PII that the law allows and its stated reasons need. */
    number_6FULL_STOP4_Gather_within_bounds = "principle_6_4",
    /** Systems and procedures are built to touch as little PII as they can, and as few people as possible can reach it. */
    number_6FULL_STOP5_A_small_footprint = "principle_6_5",
    /** PII is used, shared and kept only as far as the stated reasons go, and is safely disposed of afterwards. */
    number_6FULL_STOP6_Bounded_use_and_keeping = "principle_6_6",
    /** PII stays right, whole, up to date and suited to its use, and there are ways to check and fix it. */
    number_6FULL_STOP7_Correct_and_fit = "principle_6_7",
    /** People can easily find out what the organization does with PII, and hear about important changes. */
    number_6FULL_STOP8_Say_what_happens = "principle_6_8",
    /** People can look at the PII held about them and dispute it, within what the law allows. */
    number_6FULL_STOP9_People_see_their_own = "principle_6_9",
    /** The organization writes down its duties, keeps protection in place when PII passes to others, and handles complaints and redress. */
    number_6FULL_STOP10_Answer_for_it = "principle_6_10",
    /** Security measures at every level guard PII against loss and unauthorized reach for as long as it is held. */
    number_6FULL_STOP11_Keep_it_safe = "principle_6_11",
    /** The organization checks, and can prove, that it meets its privacy duties, through audits and regular risk assessment. */
    number_6FULL_STOP12_Show_the_rules_are_met = "principle_6_12",
};
/**
* The things an organization can do to PII.
*/
export enum PfOperation {
    
    /** Get PII from the person it is about, or from another source. */
    collect = "collect",
    /** Hold PII on a lasting medium. */
    store = "store",
    /** Fetch stored PII for use. */
    retrieve = "retrieve",
    /** Look at PII without taking a copy away. */
    consult = "consult",
    /** Change PII that is already held. */
    alter = "alter",
    /** Swap identifying details for an alias, in a way someone can still trace back. */
    pseudonymize = "pseudonymize",
    /** Change PII so that nobody can trace it back to a person again. */
    anonymize = "anonymize",
    /** Make PII available to another party. */
    disclose = "disclose",
    /** Spread PII widely, such as by publishing it. */
    disseminate = "disseminate",
    /** Remove PII so that it can no longer be reached or used. */
    delete = "delete",
    /** Remove PII and whatever carried it, beyond recovery. */
    destroy = "destroy",
};
/**
* The ways information turns out to be PII, which a record lists so that a reader can see why the item counts.
*/
export enum PfPiiRecognition {
    
    /** It singles out one person by itself, such as a passport number. */
    direct_identifier = "direct_identifier",
    /** It sets one person apart, alone or with other details, such as a rare job title in a small town. */
    distinguishing_trait = "distinguishing_trait",
    /** It says something about a person who is already known, or can be joined to a record that does. */
    linked_information = "linked_information",
    /** It holds an alias in place of an identifier, and the alias can be traced. */
    pseudonym = "pseudonym",
    /** It describes other data, such as a message's sender and time, and so reveals a person. */
    metadata = "metadata",
    /** The organization received it without asking for it. */
    unsolicited = "unsolicited",
};
/**
* How much harm the PII could do to the person it is about.
*/
export enum PfSensitivity {
    
    /** It needs the usual protection for PII. */
    ordinary = "ordinary",
    /** Its misuse could badly harm the person, or a law sets it apart, such as health data, so it needs stronger protection. */
    sensitive = "sensitive",
};
/**
* Where a requirement to safeguard PII comes from.
*/
export enum PfRequirementFactor {
    
    /** A statute, a regulation, a court's ruling or a collective agreement. */
    law = "law",
    /** An agreement between parties, such as one with a processor, or rules that bind a group of companies. */
    contract = "contract",
    /** How the business or its application works, or a code of practice it chose to follow. */
    business = "business",
    /** Another source, such as what people have said they prefer, or a technical standard the organization adopted. */
    other = "other",
};
/**
* Who a privacy policy is written for.
*/
export enum PfPolicyAudience {
    
    /** People inside the organization, who act on its commitments. */
    internal = "internal",
    /** The people whose PII it handles, who read it to learn what happens. */
    public_notice = "public_notice",
};
/**
* The form a control takes.
*/
export enum PfControlKind {
    
    /** A policy, a procedure, a role or another way of running things. */
    organizational = "organizational",
    /** A measure that guards the places and equipment where PII sits. */
    physical = "physical",
    /** A system, product or service that protects PII. */
    technical = "technical",
    /** A technical measure built to reduce what is collected or revealed about people. */
    privacy_enhancing_technology = "privacy_enhancing_technology",
    /** A binding agreement, such as one with a processor or across a group of companies. */
    contractual = "contractual",
};
/**
* How far a control has been put into effect.
*/
export enum PfImplementationState {
    
    /** It is decided on but not started. */
    planned = "planned",
    /** It is being put in place. */
    in_progress = "in_progress",
    /** It is in place and working. */
    in_operation = "in_operation",
    /** It is no longer in use. */
    retired = "retired",
};
/**
* A qualitative level of risk to people, offered for an organization that adopts it, since the framework leaves the scale to the organization.
*/
export enum PfRiskLevel {
    
    /** The harm to people would be limited. */
    low = "low",
    /** The harm would call for planned measures. */
    medium = "medium",
    /** The harm could be serious. */
    high = "high",
    /** The harm could be severe or lasting, and needs treating at once. */
    very_high = "very_high",
};
/**
* How a person's agreement to processing is obtained.
*/
export enum PfConsentMechanism {
    
    /** The person acts to agree before the processing starts. */
    opt_in = "opt_in",
    /** The processing goes ahead unless the person acts to refuse it. */
    opt_out = "opt_out",
    /** Something the person does shows agreement, such as placing an order, where the law allows that reading. */
    implied = "implied",
};
/**
* Where a person's agreement stands.
*/
export enum PfConsentState {
    
    /** The agreement holds. */
    given = "given",
    /** The person said no. */
    refused = "refused",
    /** The person took back an agreement they had given. */
    withdrawn = "withdrawn",
    /** The agreement ran out. */
    expired = "expired",
};


/**
 * What every record of the framework has, so that other records can refer to it: an identifier, a title and a description.
 */
export interface PfRecordMixin {
    /** The record's identifier, unique among the records of the framework, such as a URI or a CURIE. Other records refer to the record by it. */
    pf_id: string,
    /** The name the organization gives the record. */
    title: string,
    /** What the record says or describes, in the organization's own words. */
    description?: string,
}


/**
 * One organization's use of the privacy framework: the systems it covers, and every record the organization keeps about them, each kind in a list of its own.
 */
export interface PfFramework extends PfRecordMixin {
    /** The legal systems that apply to the record, in the organization's terms. */
    pf_jurisdictions?: string[],
    /** The organization that applies the framework. */
    pf_organization: string,
    /** The ICT systems the framework covers. */
    pf_ict_systems?: string[],
    /** Those who take part in handling the PII. */
    pf_actors?: PfActor[],
    /** The PII the organization has recognized. */
    pf_pii_items?: PfPiiItem[],
    /** The ways PII passes between the actors. */
    pf_flows?: PfPiiFlow[],
    /** What the organization does with PII. */
    pf_processing_activities?: PfProcessingActivity[],
    /** What the organization must do to safeguard PII. */
    pf_safeguarding_requirements?: PfSafeguardingRequirement[],
    /** The organization's privacy policies. */
    pf_policies?: PfPolicy[],
    /** The organization's controls. */
    pf_controls?: PfControl[],
    /** How the organization stands against each privacy principle. */
    pf_principle_implementations?: PfPrincipleImplementation[],
    /** The risks to people that the organization has identified. */
    pf_risks?: PfRisk[],
    /** The organization's privacy impact assessments. */
    pf_impact_assessments?: PfImpactAssessment[],
    /** The breaches the organization has recorded. */
    pf_breaches?: PfBreach[],
    /** The consents the organization holds. */
    pf_consents?: PfConsent[],
    /** What people have said they prefer. */
    pf_preferences?: PfPreference[],
}


/**
 * Someone who takes part in handling PII, told apart by the part they play. One party can play different parts for different PII, with a record for each.
 */
export interface PfActor extends PfRecordMixin {
    /** The kind of actor: PfPiiPrincipal, PfPiiController, PfPiiProcessor or PfThirdParty. */
    pf_actor_type: string,
    /** The legal systems that apply to the record, in the organization's terms. */
    pf_jurisdictions?: string[],
    /** How to reach the actor about privacy. */
    pf_contact?: string,
}


/**
 * The person the PII is about, or a group of such people when the organization records them together.
 */
export interface PfPiiPrincipal extends PfActor {
}


/**
 * The party that decides why and how PII is processed, and answers for it even when another party does the work.
 */
export interface PfPiiController extends PfActor {
    /** The reasons the PII is processed, in the organization's own words. */
    pf_purposes?: string[],
    /** What makes the processing lawful, in the terms of the law that applies. */
    pf_legal_bases?: string[],
    /** The processors that work for the controller. */
    pf_appointed_processors?: PfPiiProcessorPfId[],
    /** The privacy policy the controller works under. */
    pf_controller_policy?: PfPolicyPfId,
    /** The person who advises the controller on privacy, where there is one. */
    pf_privacy_officer?: string,
}


/**
 * A party that processes PII for a controller, on that controller's instructions.
 */
export interface PfPiiProcessor extends PfActor {
    /** The controllers whose instructions the processor follows. */
    pf_instructing_controllers?: PfPiiControllerPfId[],
    /** The reference of the agreement that binds the processor, where there is one. */
    pf_processing_agreement?: string,
    /** The processors this processor has engaged in turn. */
    pf_sub_processors?: PfPiiProcessorPfId[],
}


/**
 * A party outside the controller and its processors that receives PII for its own ends, and usually becomes a controller of that PII.
 */
export interface PfThirdParty extends PfActor {
    /** What the third party receives the PII for. */
    pf_receiving_purpose?: string,
    /** What makes the passing of PII to the third party lawful. */
    pf_transfer_basis?: string,
}


/**
 * A piece or set of information that can be tied to a person, why it counts as PII, how sensitive it is and how it is handled.
 */
export interface PfPiiItem extends PfRecordMixin {
    /** The people the PII of the record is about. */
    pf_concerned_principals?: PfPiiPrincipalPfId[],
    /** The things done to the PII. */
    pf_operations?: string,
    /** How long the PII is kept, as an ISO 8601 duration. */
    pf_retention?: string,
    /** What the item holds, in the organization's own words. */
    pf_pii_categories?: string[],
    /** Why the information counts as PII. */
    pf_recognized_by?: string,
    /** How sensitive the item is. */
    pf_sensitivity?: string,
    /** Whether an alias stands in for the item's identifying details. */
    pf_pseudonymized?: boolean,
    /** How easily the item could be joined with other data to identify someone, in the organization's words. */
    pf_linkability?: string,
}


/**
 * One way PII passes from one actor to another, and who decides what happens to it afterwards.
 */
export interface PfPiiFlow extends PfRecordMixin {
    /** The PII items the record concerns. */
    pf_concerned_pii?: PfPiiItemPfId[],
    /** The actor the PII comes from. */
    pf_provider: PfActorPfId,
    /** The actor the PII goes to. */
    pf_recipient: PfActorPfId,
    /** The actor that decides what happens to the PII once it has passed. A processor never holds this position. */
    pf_decides_afterwards?: PfActorPfId,
}


/**
 * Something the organization does with PII: why, on what basis, what it does to which PII, who is responsible, and how long the PII is kept.
 */
export interface PfProcessingActivity extends PfRecordMixin {
    /** The reasons the PII is processed, in the organization's own words. */
    pf_purposes?: string[],
    /** What makes the processing lawful, in the terms of the law that applies. */
    pf_legal_bases?: string[],
    /** The things done to the PII. */
    pf_operations?: string,
    /** The PII items the record concerns. */
    pf_concerned_pii?: PfPiiItemPfId[],
    /** How long the PII is kept, as an ISO 8601 duration. */
    pf_retention?: string,
    /** The organization's controls that act on the record's subject. */
    pf_related_controls?: PfControlPfId[],
    /** The controller that answers for the activity. */
    pf_controller: PfPiiControllerPfId,
    /** The processors that do the work. */
    pf_processors?: PfPiiProcessorPfId[],
    /** The flows of PII the activity involves. */
    pf_activity_flows?: PfPiiFlowPfId[],
    /** The levels of sensitivity among the PII involved. */
    pf_sensitivities?: string,
    /** Whether PII leaves the jurisdiction it was collected in. */
    pf_crosses_borders?: boolean,
    /** What protects the PII when it crosses a border. */
    pf_transfer_safeguards?: string[],
}


/**
 * Something the organization must do to protect PII, and where that duty comes from.
 */
export interface PfSafeguardingRequirement extends PfRecordMixin {
    /** Where the requirement comes from. */
    pf_requirement_factor: string,
    /** The law, contract or other document that states it. */
    pf_requirement_source?: string,
    /** The actors that must meet it. */
    pf_applies_to?: PfActorPfId[],
    /** The controls that meet it. */
    pf_met_by?: PfControlPfId[],
}


/**
 * A privacy policy: what the organization commits to about PII, written for its own people or as a notice to the people whose PII it handles.
 */
export interface PfPolicy extends PfRecordMixin {
    /** The reasons the PII is processed, in the organization's own words. */
    pf_purposes?: string[],
    /** The PII items the record concerns. */
    pf_concerned_pii?: PfPiiItemPfId[],
    /** The privacy principles the record bears on. */
    pf_principles?: string,
    /** Who the policy is written for. */
    pf_policy_audience: string,
    /** The version of the policy. */
    pf_policy_version?: string,
    /** What the policy covers. */
    pf_policy_scope?: string,
    /** When the policy takes effect. */
    pf_policy_effective_date?: date,
    /** When the policy was last reviewed. */
    pf_policy_last_reviewed?: date,
    /** What the policy says about how long PII is kept. */
    pf_retention_statement?: string,
    /** The rights the policy tells people they have. */
    pf_stated_rights?: string[],
    /** Where people can send questions about the policy. */
    pf_inquiry_contact?: string,
}


/**
 * A measure that treats a privacy risk by making it less likely or less harmful, the principles it serves and how far it has been put into effect.
 */
export interface PfControl extends PfRecordMixin {
    /** The privacy principles the record bears on. */
    pf_principles?: string,
    /** What shows that the record's claim holds, such as a report or a log. */
    pf_evidence?: string[],
    /** The form the control takes. */
    pf_control_kind: string,
    /** What the control is meant to achieve. */
    pf_control_objective?: string,
    /** How the control is put into effect. */
    pf_control_detail?: string,
    /** The actor that answers for the control. */
    pf_control_responsible?: PfActorPfId,
    /** How far the control has been put into effect. */
    pf_control_state?: string,
    /** The safeguarding requirements the control answers to. */
    pf_answers_requirements?: PfSafeguardingRequirementPfId[],
}


/**
 * How the organization stands against one privacy principle: what it does, what shows it, and what is still missing.
 */
export interface PfPrincipleImplementation extends PfRecordMixin {
    /** The organization's controls that act on the record's subject. */
    pf_related_controls?: PfControlPfId[],
    /** What shows that the record's claim holds, such as a report or a log. */
    pf_evidence?: string[],
    /** The principle the record is about. */
    pf_principle: string,
    /** What the organization does to follow the principle. */
    pf_measures?: string[],
    /** Where the organization falls short. */
    pf_gaps?: string[],
    /** What the organization will do about the gaps. */
    pf_improvements?: string[],
    /** When the organization last checked its standing. */
    pf_last_assessed?: date,
}


/**
 * A way that handling PII could harm people: where the risk comes from, how likely and how bad it is, and what is done about it.
 */
export interface PfRisk extends PfRecordMixin {
    /** The PII items the record concerns. */
    pf_concerned_pii?: PfPiiItemPfId[],
    /** The people the PII of the record is about. */
    pf_concerned_principals?: PfPiiPrincipalPfId[],
    /** The organization's controls that act on the record's subject. */
    pf_related_controls?: PfControlPfId[],
    /** Where the risk comes from. */
    pf_risk_source?: string,
    /** How likely the harm is, in the organization's own terms. */
    pf_risk_likelihood?: string,
    /** What the harm to people would be. */
    pf_risk_consequence?: string,
    /** The risk's level before controls. */
    pf_risk_inherent_level?: string,
    /** The risk's level after controls, which is never above the level before. */
    pf_risk_residual_level?: string,
    /** The person who answers for the risk. */
    pf_risk_owner?: string,
}


/**
 * A review of what a system or activity could do to people's privacy, the risks it found and what became of them.
 */
export interface PfImpactAssessment extends PfRecordMixin {
    /** What the assessment looks at. */
    pf_assessment_scope?: string,
    /** When the assessment was done. */
    pf_assessment_date?: date,
    /** Who did the assessment. */
    pf_assessor?: string,
    /** The processing activities it looks at. */
    pf_assessed_activities?: PfProcessingActivityPfId[],
    /** The risks it found. */
    pf_risks_found?: PfRiskPfId[],
    /** Those of the risks found that have been treated. */
    pf_risks_treated?: PfRiskPfId[],
    /** Those of the risks found that the organization has accepted as they stand. */
    pf_risks_accepted?: PfRiskPfId[],
    /** What the assessment concluded. */
    pf_assessment_outcome?: string,
    /** Who was asked, and what they said. */
    pf_consultations?: string[],
    /** When the next assessment is due, which is after this one. */
    pf_next_assessment?: date,
}


/**
 * A time when PII was handled against a safeguarding requirement: what happened, who was told and what was done.
 */
export interface PfBreach extends PfRecordMixin {
    /** The PII items the record concerns. */
    pf_concerned_pii?: PfPiiItemPfId[],
    /** When the breach happened. */
    pf_breach_occurred?: string,
    /** When the organization found out, which is not before it happened. */
    pf_breach_discovered?: string,
    /** When the organization closed the matter, which is not before it found out. */
    pf_breach_closed?: string,
    /** How many people the breach reached, where that is known. */
    pf_principals_affected?: number,
    /** The safeguarding requirements the breach went against. */
    pf_breached_requirements?: PfSafeguardingRequirementPfId[],
    /** How serious the breach is. */
    pf_breach_severity?: string,
    /** What was done straight away. */
    pf_immediate_actions?: string[],
    /** Whether a law or contract requires anyone to be told. */
    pf_notification_required?: boolean,
    /** Who was told, and when. */
    pf_notifications?: string[],
    /** What was done to put things right. */
    pf_remediation?: string[],
    /** What the organization learned. */
    pf_lessons?: string,
}


/**
 * One person's agreement to the processing of their PII for stated purposes, and where it stands.
 */
export interface PfConsent extends PfRecordMixin {
    /** The reasons the PII is processed, in the organization's own words. */
    pf_purposes?: string[],
    /** The PII items the record concerns. */
    pf_concerned_pii?: PfPiiItemPfId[],
    /** What shows that the record's claim holds, such as a report or a log. */
    pf_evidence?: string[],
    /** The person the record is about. */
    pf_principal: PfPiiPrincipalPfId,
    /** How the agreement was obtained. */
    pf_consent_mechanism?: string,
    /** When the person agreed. */
    pf_consent_given?: string,
    /** Where the agreement stands. */
    pf_consent_state: string,
    /** When the person took the agreement back. */
    pf_consent_withdrawn?: string,
}


/**
 * What one person has said they want done, or not done, with their PII.
 */
export interface PfPreference extends PfRecordMixin {
    /** The person the record is about. */
    pf_principal: PfPiiPrincipalPfId,
    /** What the preference applies to. */
    pf_preference_scope?: string,
    /** Whether the person asks not to be identified at all. */
    pf_wants_anonymity?: boolean,
    /** Whether the person asks to appear under an alias. */
    pf_wants_pseudonymity?: boolean,
    /** What the person does not want done to their PII. */
    pf_refused_operations?: string,
    /** Who the person does not want their PII passed to. */
    pf_refused_recipients?: string[],
    /** When the organization recorded the preference. */
    pf_preference_recorded?: date,
}



