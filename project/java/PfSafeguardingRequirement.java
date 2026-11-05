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
  Something the organization must do to protect PII, and where that duty comes from.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PfSafeguardingRequirement  {

  private String pfRequirementFactor;
  private String pfRequirementSource;
  private List<PfActor> pfAppliesTo;
  private List<PfControl> pfMetBy;
  private URI pfId;
  private String title;
  private String description;


}