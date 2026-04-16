package None;

/* metamodel_version: 1.7.0 */
/* version: 1.0.0 */
import java.util.List;
import lombok.*;

/**
  Schema class for a protective measure that manages privacy risks within the framework. Can be organizational, physical, technical (including Privacy Enhancing Technologies), or legal-contractual in nature; linked to the principles and safeguarding requirements it addresses.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PrivacyControl extends NamedEntity {

  private String controlType;
  private String controlObjective;
  private List<String> addressedPrinciples;
  private String implementationDescription;
  private String responsibleActor;
  private String implementationStatus;
  private List<String> effectivenessEvidence;
  private List<PrivacySafeguardingRequirement> relatedSafeguardingRequirements;
  private boolean isPet;

}