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
  Someone who takes part in handling PII, told apart by the part they play. One party can play different parts for different PII, with a record for each.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class PfActor  {

  private String pfActorType;
  private List<String> pfJurisdictions;
  private String pfContact;
  private URI pfId;
  private String title;
  private String description;


}