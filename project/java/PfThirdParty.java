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
  A party outside the controller and its processors that receives PII for its own ends, and usually becomes a controller of that PII.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PfThirdParty extends PfActor {

  private String pfReceivingPurpose;
  private String pfTransferBasis;


}