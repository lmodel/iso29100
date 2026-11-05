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
  A measure that treats a privacy risk by making it less likely or less harmful, the principles it serves and how far it has been put into effect.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PfControl  {

  private List<String> pfPrinciples;
  private List<String> pfEvidence;
  private String pfControlKind;
  private String pfControlObjective;
  private String pfControlDetail;
  private PfActor pfControlResponsible;
  private String pfControlState;
  private List<PfSafeguardingRequirement> pfAnswersRequirements;
  private URI pfId;
  private String title;
  private String description;


}