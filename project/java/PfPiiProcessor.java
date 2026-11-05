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
  A party that processes PII for a controller, on that controller's instructions.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PfPiiProcessor extends PfActor {

  private List<PfPiiController> pfInstructingControllers;
  private String pfProcessingAgreement;
  private List<PfPiiProcessor> pfSubProcessors;


}