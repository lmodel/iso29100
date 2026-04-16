package None;

/* metamodel_version: 1.7.0 */
/* version: 1.0.0 */
import java.util.List;
import lombok.*;

/**
  Schema base class for the four actor types recognized by the privacy framework: PII principals, PII controllers, PII processors, and third parties. Provides shared contact and jurisdictional attributes common to all stakeholder roles.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class PrivacyStakeholder extends NamedEntity {

  private String contactInformation;
  private List<String> jurisdictions;

}