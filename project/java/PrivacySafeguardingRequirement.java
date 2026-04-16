package None;

/* metamodel_version: 1.7.0 */
/* version: 1.0.0 */
import java.util.List;
import lombok.*;

/**
  Schema class for an applicable requirement that drives an organization's PII processing controls. Requirements are identified through the privacy risk management process and arise from legal/regulatory, contractual, business, or other influencing factors.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PrivacySafeguardingRequirement extends NamedEntity {

  private String requirementFactor;
  private String requirementText;
  private String sourceReference;
  private List<String> applicableToActors;
  private List<PrivacyControl> relatedControls;
  private String priority;

}