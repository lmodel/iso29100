package None;

/* metamodel_version: 1.7.0 */
/* version: 1.0.0 */
import java.util.List;
import lombok.*;

/**
  Schema class for a structured evaluation of the privacy implications of a processing activity or ICT system. Records assessment scope, identified and treated risks, accepted residual risks, stakeholder consultation records, and overall assessment outcome.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PrivacyImpactAssessment extends NamedEntity {

  private String assessmentScope;
  private LocalDate assessmentDate;
  private String assessor;
  private List<PIIProcessingActivity> processingActivitiesAssessed;
  private List<PrivacyRisk> risksIdentified;
  private List<PrivacyRisk> risksTreated;
  private List<PrivacyRisk> residualRisksAccepted;
  private String assessmentOutcome;
  private LocalDate nextAssessmentDate;
  private List<String> consultationRecords;

}