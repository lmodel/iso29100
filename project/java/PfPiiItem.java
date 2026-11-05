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
  A piece or set of information that can be tied to a person, why it counts as PII, how sensitive it is and how it is handled.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PfPiiItem  {

  private List<PfPiiPrincipal> pfConcernedPrincipals;
  private List<String> pfOperations;
  private String pfRetention;
  private List<String> pfPiiCategories;
  private List<String> pfRecognizedBy;
  private String pfSensitivity;
  private Boolean pfPseudonymized;
  private String pfLinkability;
  private URI pfId;
  private String title;
  private String description;


}