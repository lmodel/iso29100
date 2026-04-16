package None;

/* metamodel_version: 1.7.0 */
/* version: 1.0.0 */
import java.util.List;
import lombok.*;

/**
  Schema class for an external entity that receives PII outside the PII processor relationship — i.e., as a recipient that typically becomes a PII controller in its own right. Captures the receiving purpose and the legal basis for the transfer.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ThirdParty extends PrivacyStakeholder {

  private String receivingPurpose;
  private String transferBasis;

}