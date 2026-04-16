package None;

/* metamodel_version: 1.7.0 */
/* version: 1.0.0 */
import java.util.List;
import lombok.*;

/**
  Schema class representing a potential adverse outcome for PII principals from a PII processing activity. Captures the risk source, likelihood and impact assessments, inherent and residual risk levels, and links to mitigating controls and accountable risk owner.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PrivacyRisk extends NamedEntity {

  private String riskSource;
  private List<String> affectedPiiCategories;
  private String affectedPrincipalsDescription;
  private String riskLikelihood;
  private String riskImpactDescription;
  private String inherentRiskLevel;
  private String residualRiskLevel;
  private List<PrivacyControl> mitigatingControls;
  private String riskOwner;

}