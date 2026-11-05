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
  How the organization stands against one privacy principle: what it does, what shows it, and what is still missing.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PfPrincipleImplementation  {

  private List<PfControl> pfRelatedControls;
  private List<String> pfEvidence;
  private String pfPrinciple;
  private List<String> pfMeasures;
  private List<String> pfGaps;
  private List<String> pfImprovements;
  private LocalDate pfLastAssessed;
  private URI pfId;
  private String title;
  private String description;


}