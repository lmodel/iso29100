package example;

/* metamodel_version: 1.12.0 */
/* version: 2024 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A privacy policy: what the organization commits to about PII, written for its own people or as a notice to the people whose PII it handles.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PfPolicy  {

  private List<String> pfPurposes;
  private List<PfPiiItem> pfConcernedPii;
  private List<String> pfPrinciples;
  private String pfPolicyAudience;
  private String pfPolicyVersion;
  private String pfPolicyScope;
  private LocalDate pfPolicyEffectiveDate;
  private LocalDate pfPolicyLastReviewed;
  private String pfRetentionStatement;
  private List<String> pfStatedRights;
  private String pfInquiryContact;
  private URI pfId;
  private String title;
  private String description;


}