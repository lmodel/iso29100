package None;

/* metamodel_version: 1.7.0 */
/* version: 1.0.0 */
import java.util.List;
import lombok.*;

/**
  Schema class for an organization engaged to process PII under a PII controller's instructions. Records the instructing controller, data processing agreement reference, and any sub-processors engaged on the controller's behalf.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PIIProcessor extends PrivacyStakeholder {

  private PIIController instructingController;
  private String processingAgreementRef;
  private List<PIIProcessor> subProcessors;

}