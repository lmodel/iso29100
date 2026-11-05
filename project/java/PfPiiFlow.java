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
  One way PII passes from one actor to another, and who decides what happens to it afterwards.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PfPiiFlow  {

  private List<PfPiiItem> pfConcernedPii;
  private PfActor pfProvider;
  private PfActor pfRecipient;
  private PfActor pfDecidesAfterwards;
  private URI pfId;
  private String title;
  private String description;


}