package None;

/* metamodel_version: 1.7.0 */
/* version: 1.0.0 */
import java.util.List;
import lombok.*;

/**
  A documented scenario describing the flow of PII among privacy framework actors (PII principal, PII controller, PII processor, and third party), as illustrated in Table 1 of Clause 5.3.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PIIFlowScenario extends NamedEntity {

  private String scenarioLabel;
  private String piiPrincipalRole;
  private String piiControllerRole;
  private String piiProcessorRole;
  private String thirdPartyRole;
  private String scenarioDescription;
  private String legalControlRetention;

}