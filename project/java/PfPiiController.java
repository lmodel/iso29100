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
  The party that decides why and how PII is processed, and answers for it even when another party does the work.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PfPiiController extends PfActor {

  private List<String> pfPurposes;
  private List<String> pfLegalBases;
  private List<PfPiiProcessor> pfAppointedProcessors;
  private PfPolicy pfControllerPolicy;
  private String pfPrivacyOfficer;


}