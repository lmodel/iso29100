package None;

/* metamodel_version: 1.7.0 */
/* version: 1.0.0 */
import java.util.List;
import lombok.*;

/**
  Top-level container representing an organization's privacy framework for protecting PII within ICT systems.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PrivacyFramework extends NamedEntity {

  private String organizationName;
  private String ictSystemDescription;
  private List<String> applicableJurisdictions;
  private List<PIIController> piiControllers;
  private List<PIIProcessor> piiProcessors;
  private List<ThirdParty> thirdParties;
  private String piiPrincipalsDescription;
  private PrivacyPolicy privacyPolicy;
  private List<PrivacyControl> privacyControls;
  private List<PrivacySafeguardingRequirement> safeguardingRequirements;
  private List<PrivacyRisk> privacyRisks;
  private List<PrivacyImpactAssessment> privacyImpactAssessments;
  private List<PrivacyBreach> privacyBreaches;
  private List<PIIProcessingActivity> piiProcessingActivities;
  private List<PrivacyPrincipleImplementation> principleImplementations;

}